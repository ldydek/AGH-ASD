# f(i, j) - minimalny koszt dojścia do pola tab[i][j] z pola tab[0][0]
# f(i, j) = min(tab[i-1][j], tab[i][j-1]) + tab[i][j]
from math import inf


def traverse(tab):
    n = len(tab)
    aux_tab = [[inf for _ in range(n)] for _ in range(n)]
    aux_tab[0][0] = tab[0][0]
    for x in range(1, n):
        aux_tab[x][0] = aux_tab[x-1][0] + tab[x][0]
        aux_tab[0][x] = aux_tab[0][x-1] + tab[0][x]
    for x in range(1, n):
        for y in range(1, n):
            aux_tab[x][y] = min(aux_tab[x-1][y], aux_tab[x][y-1]) + tab[x][y]
    return aux_tab[n-1][n-1]


tab = [[1, 8, 7, 1], [1, 3, 4, 5], [1, 3, 3, 2], [1, 1, 1, 1]]
print(traverse(tab))
