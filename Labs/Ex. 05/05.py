# f(i, j) - optymalny podział tablicy składającej się z wyrazów od A[0] do A[i] na j części
# f(i, j) = max(min(f(k, j-1), sum(k+1, i))), gdzie 0 <= k <= i-1
# f(i, 0) = 0
# f(0, j) = 1 - gdy j = 1, 0 - wpp
# f(i, 1) = sum(0, i)
# sum(k+1, i-k-1) - suma elementów tablicy pomiędzy tymi argumentami

def sum(tab, x, y):
    if x > 0:
        return tab[y] - tab[x-1]
    return tab[y]


def ex05(tab, k):
    n = len(tab)
    for x in range(1, n):
        tab[x] += tab[x-1]
    aux_tab = [[0 for _ in range(k+1)] for _ in range(n)]
    aux_tab[0][1] = tab[0]
    for x in range(n):
        aux_tab[x][1] = tab[x]
    for x in range(1, n):
        for y in range(2, k+1):
            value = -10**10
            for z in range(x):
                value = max(value, min(aux_tab[z][y-1], sum(tab, z+1, x)))
            aux_tab[x][y] = value
    return aux_tab[n-1][k]


tab = [1, 2, 4, 6, 3, 2, 10, 3, 4, 2]
print(ex05(tab, 5))
