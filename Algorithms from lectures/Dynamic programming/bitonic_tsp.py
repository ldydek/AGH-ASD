# f(i, j) - minimalny koszt ścieżek z 0 do "i" oraz z 0 do "j", które używają łącznie wszystkie miasta {0,...,j}, ale
# żadnego nie powtarzają
# Rekursja:
# 1) jeśli i < j-1 => f(i, j) = f(i, j-1) + d(j-1, j)
# 2) jeśli i = j-1 => f(j-1, j) = min(f(k, j-1) + d(k, j)), gdzie 0 <= k < j-1
# Rozwiązanie: min(f(i, n-1)+d(i, n-1)), gdzie 0 <= i < n-1
# Złożoność czasowa: O(n^2 + n^2) = O(n^2)
# Złożoność pamięciowa: O(n^2)
from math import inf


def distance(x, y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2) ** (1/2)


def bitonic_tsp(cities):
    n = len(cities)
    aux_tab = [[inf for _ in range(n)] for _ in range(n)]
    aux_tab[0][1] = distance(cities[0], cities[1])
    for x in range(2, n):
        aux_tab[0][x] = aux_tab[0][x-1] + distance(cities[x-1], cities[x])
    for x in range(1, n):
        for y in range(x+1, n):
            if x < y-1:
                aux_tab[x][y] = aux_tab[x][y-1] + distance(cities[y-1], cities[y])
            else:
                best = inf
                for z in range(y-1):
                    best = min(best, aux_tab[z][y-1] + distance(cities[z], cities[y]))
                aux_tab[x][y] = best
    return print_solution(aux_tab, cities)


def print_solution(aux_tab, cities):
    solution = inf
    n = len(aux_tab)
    for x in range(n-1):
        solution = min(solution, aux_tab[x][n-1] + distance(cities[x], cities[n-1]))
    return solution


cities = [(0, 6), (1, 0), (2, 3), (5, 4), (6, 1), (7, 5), (8, 2)]
print(bitonic_tsp(cities))
