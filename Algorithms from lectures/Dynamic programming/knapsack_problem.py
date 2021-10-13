# Problem plecakowy.
# f(i, w) - maksymalny koszt jaki można uzyskać, biorąc pod uwagę przedmioty od tab[0] do tab[i]
# i nie przekraczając wagi "w"
# f(0, w) = 0
# f(i, 0) = 0
# f(i, w) = max(f(i-1, w), f(i-1, w-W[i]) + P[i])
# Spamiętywanie daje zły wynik
from math import inf


def knapsack_problem(W, P, max_w):
    n = len(W)
    aux_tab = [[0 for _ in range(max_w+1)] for _ in range(n)]
    for x in range(W[0], max_w+1):
        aux_tab[0][x] = P[0]
    for x in range(1, n):
        for y in range(1, max_w+1):
            aux_tab[x][y] = aux_tab[x-1][y]
            if y >= W[x]:
                aux_tab[x][y] = max(aux_tab[x][y], aux_tab[x-1][y-W[x]]+P[x])
    return aux_tab


def knapsack_problem_memoized(W, P, max_w):
    n = len(W)
    aux_tab = [[inf for _ in range(max_w+1)] for _ in range(n)]
    for x in range(n):
        aux_tab[x][0] = 0
    for x in range(W[0], max_w+1):
        aux_tab[0][x] = P[0]
    for x in range(W[0]):
        aux_tab[0][x] = 0
    reku(aux_tab, W, P, n-1, max_w)
    return aux_tab


def reku(aux_tab, W, P, n, max_w):
    if aux_tab[n][max_w] != inf:
        return aux_tab[n][max_w]
    xd = -inf
    if max_w >= W[n]:
        xd = max(reku(aux_tab, W, P, n-1, max_w), reku(aux_tab, W, P, n-1, max_w - W[n]) + P[n])
        aux_tab[n][max_w] = xd
    return xd


val = [600, 100, 120, 1000, 2000]
wt = [5, 20, 30, 5, 10]
W = 50
print(knapsack_problem(wt, val, 50))
print(knapsack_problem_memoized(wt, val, 50))
