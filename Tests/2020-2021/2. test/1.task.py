# f(i, j) - maksymalna liczba studentów, jaka może mieszkać w akademikach ze zbioru od A[0] do A[i], nie przekraczając
# ceny "j"
# albo dany akademik budejemy albo nie, więc rekursja wygląda następująco:
# f(i, j) = max(f(i-1, j), f(prev(i), j-cena(i))+student(i))
# prev(i) - pierwszy akademik na lewo od rozważanego, który na niego nie nachodzi (niekoniecznie jest to i-1!)
# zadanie w pewien sposób podobne do problemu plecakowego
# Złożonośc czasowa: O(np + n log n)
# Złożoność pamięciowa: O(np)
# Passed all tests

def binary_search(tab, k):
    n = len(tab)
    l, r = 0, n - 1
    index = None
    while l <= r:
        m = (l + r) // 2
        if tab[m][2] >= k[1]:
            r = m - 1
        else:
            index = m
            l = m + 1
    if index is not None:
        return index
    return False


def show_previous(T, prev):
    for x in range(len(T)):
        T[x] = (T[x][0], T[x][1], T[x][2], T[x][3], x)
    T.sort(key=lambda x: x[2], reverse=True)
    T.sort(key=lambda x: x[1])
    for x in range(len(T)):
        sol = binary_search(T, T[x])
        if sol is not False:
            prev[x] = sol


def surface(x):
    return (x[2]-x[1])*x[0]


def find_index(aux_tab):
    index, val = None, 0
    n = len(aux_tab)
    for x in range(len(aux_tab[n-1])):
        if aux_tab[n-1][x] > val:
            val = aux_tab[n-1][x]
            index = x
    return index


def select_buildings(T, p):
    n = len(T)
    prev = [-1] * n
    show_previous(T, prev)
    aux_tab = [[0 for _ in range(p)] for _ in range(n)]
    for x in range(T[0][3], p):
        aux_tab[0][x] = surface(T[0])
    for x in range(1, n):
        for y in range(p):
            aux_tab[x][y] = aux_tab[x-1][y]
            if y >= T[x][3]:
                aux_tab[x][y] = max(aux_tab[x][y], aux_tab[prev[x]][y-T[x][3]]+surface(T[x]))
    index = find_index(aux_tab)
    return print_solution(T, aux_tab, index)


def print_solution(T, aux_tab, p):
    solution = []
    for x in range(len(aux_tab)-1, 0, -1):
        if aux_tab[x][p] != aux_tab[x-1][p]:
            solution.append(T[x][4])
            p -= T[x][3]
    if T[0][3] <= p:
        solution.append(T[0][4])
    solution.sort()
    return solution


T = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
p = 6
print(select_buildings(T, p))

