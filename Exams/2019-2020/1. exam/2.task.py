# Dynamic programming approach
# f(i, j) - way of adding numbers from A[i] to A[j], which highest temporary score is the lowest from all highest
# temporary scores
# recursion: f(i, j) = min(max(f(i, k), f(k+1, j), |sum(i, j)|), where sum(i, j) means sum of all elements between
# A[i] and A[j] also including A[i] and A[j] and i <= k <= j-1
# solution: f(0, n-1)
# In other words we want to find f(i, j), so we try to divide (A[i],...,A[j]) into two parts of the lowest temporary
# scores and these subproblems were computed before and can be included in a final solution (optimal substructure).
# Passed all tests
from math import inf


def sum(tab, x, y):
    if x == 0:
        return tab[y]
    return tab[y]-tab[x-1]


def opt_sum(tab):
    n = len(tab)
    for x in range(1, n):
        tab[x] += tab[x-1]
    aux_tab = [[inf for _ in range(n)] for _ in range(n)]
    for x in range(n):
        aux_tab[x][x] = abs(sum(tab, x, x))
    for x in range(n-1):
        aux_tab[x][x+1] = abs(sum(tab, x, x+1))
    for y in range(2, n):
        index = y
        x = 0
        while x + index < n:
            best = inf
            for z in range(x, x+index):
                if z == x:
                    best = max(min(best, aux_tab[x+1][x+index]), abs(sum(tab, x, y)))
                if z == x+index-1:
                    best = max(min(best, aux_tab[x][x+index-1]), abs(sum(tab, x, y)))
                else:
                    best = min(best, max(aux_tab[x][z], aux_tab[z+1][x+index], abs(sum(tab, x, y))))
            if index == 2:
                best = max(abs(sum(tab, x, x+index)), min(aux_tab[x][x+1], aux_tab[x+1][x+index]))
            aux_tab[x][x+index] = best
            x += 1
    return aux_tab[0][n-1]


tab = [-999, -1000, 1001, 1000]
print(opt_sum(tab))
