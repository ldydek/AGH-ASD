# f(i, j) - minimalna ilość skoków, jakie musi wykonać żaba, aby dostać się na pole A[i], mając "j" jednostek energii
# przed zjedzeniem
# f(i, j) = min(f(i-k, j+k-A[i])) + 1, gdzie 1 <= k <= j-A[i] oraz zachodzi warunek i >= k
# j - A[i] to energia żaby przed zjedzeniem przekąski a więc maksymalnie o tyle miejsc można patrzeć do tyłu (jeśli
# patrzylibyśmy dalej, to energia żaby musiałaby być ujemna)
# Rozwiązanie: f(n-1, j) gdzie "j" to pewna ilość energii żaby na ostatnim polu
# Warunki brzegowe: f(0, A[0]) = 0 oraz f(0, j\A[0]) = -1, ponieważ taka sytuacja nie jest możliwa
# Złożoność czasowa: O(nk)
# Złożoność pamięciowa: O(nk), gdzie "k" to suma energii ze wszystkich kamieni
# Bonusowo odtwarzanie rozwiązania.
from math import inf


def find_index(aux_tab):
    k = len(aux_tab[0])
    n, index = len(aux_tab), None
    for x in range(k-1, -1, -1):
        if aux_tab[n-1][x] != inf:
            index = (n-1, x)
            return index


def ex04(tab):
    n = len(tab)
    k = sum(tab)
    aux_tab = [[inf for _ in range(k)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(k)] for _ in range(n)]
    aux_tab[0][tab[0]] = 0
    for x in range(1, n):
        for y in range(tab[x], k):
            mini = inf
            for z in range(1, x+1):
                if y + z - tab[x] < k:
                    if mini > aux_tab[x-z][y+z-tab[x]]:
                        mini = aux_tab[x-z][y+z-tab[x]]
                        parent[x][y] = (x-z, y+z-tab[x])
            aux_tab[x][y] = mini + 1
            if y >= n-1-x and aux_tab[x][y] != inf:
                aux_tab[n-1][y-n+1+x] = aux_tab[x][y] + 1
                parent[n-1][y-n+1+x] = (x, y)
                index = find_index(aux_tab)
                return print_solution(index, parent)
    index = find_index(aux_tab)
    return print_solution(index, parent)


def print_solution(index, parent):
    solution = []
    while parent[index[0]][index[1]] != (-1, -1):
        solution.append(parent[index[0]][index[1]][0])
        index = parent[index[0]][index[1]]
    return solution[::-1]


tab = [2, 1, 100, 1, 1, 2, 1, 0]
print(ex04(tab))
