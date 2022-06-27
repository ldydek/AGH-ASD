# f(i, j) - minimalny koszt pomnożenia macierzy od Ai do Aj
# f(i, j) = min(f(i, k) + f(k+1, j) + pqr), gdzie pqr to koszt pomnożenia ze sobą dwóch macierzy o wymiarach p x q i
# q x r, i <= k <= j-1
# Warunki brzegowe: f(i, i) = 0
# Rozwiązanie: f(0, n-1)


def ex04(sizes):
    n = len(sizes) - 1
    aux_tab = [[-1 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        aux_tab[x][x] = 0
    for x in range(n):
        for y in range(x+1, n):
            ctr = 10**10
            for z in range(y-x-1, y):
                ctr = min(ctr, aux_tab[y-x-1][z]+aux_tab[z+1][y]+sizes[y-x-1]*sizes[z+1]*sizes[y+1])
            aux_tab[y-x-1][y] = ctr
    return aux_tab[0][n-1]


sizes = [30, 35, 15, 5, 10, 20, 25]
print(ex04(sizes))
