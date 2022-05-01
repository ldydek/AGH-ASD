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


def sum_of_values(tab, x, y):
    if x == 0:
        return tab[y]
    return tab[y] - tab[x-1]


def opt_sum(tab):
    n = len(tab)
    dp = [[-inf for _ in range(n)] for _ in range(n)]
    for x in range(1, n):
        tab[x] += tab[x-1]
    for y in range(1, n):
        index1, index2 = 0, y
        while index2 < n:
            value = inf
            for k in range(y):
                if k == 0:
                    value = max(abs(sum_of_values(tab, index1, index2)), dp[index1+1][index2])
                elif k == y-1:
                    value = min(value, max(abs(sum_of_values(tab, index1, index2)), dp[index1][index2-1]))
                else:
                    value = min(value, max(dp[index1][index1+k], dp[index1+k+1][index2], abs(sum_of_values(tab, index1, index2))))
            dp[index1][index2] = value
            index1 += 1
            index2 += 1
    return dp[0][n-1]


tab = [-999, -1000, 1001, 1000]
print(opt_sum(tab))
