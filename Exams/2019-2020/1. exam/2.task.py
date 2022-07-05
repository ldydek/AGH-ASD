# Dynamic programming approach
# f(i, j) - way of adding numbers from A[i] to A[j], which highest temporary score is the lowest from all highest
# temporary scores
# recursion: f(i, j) = min(max(f(i, k), f(k+1, j)), where i+1 <= k <= j-2 - this case happens when in each bracket
# there are at least two numbers. Unfortunately, we have an exception when in a certain bracket there will be only
# one number. This recursion provides that:
# f(i, j) = max(sum(i, j), min(f(i, j-1), f(i+1, j)), where sum(i, j) means sum of all elements between
# A[i] and A[j] also including A[i] and A[j]
# At the end, to compute f(i, j) we take minimum from both these cases.
# solution: f(0, n-1)
# In other words we want to find f(i, j), so we try to divide (A[i],...,A[j]) into two parts of the lowest temporary
# scores and these subproblems were computed before and can be included in a final solution (optimal substructure).
# Time complexity: O(n^3)
# Space complexity: O(n^2)
# Passed all tests

# prefix sum method
def prefix_sum(tab):
    n = len(tab)
    for x in range(1, n):
        tab[x] += tab[x-1]


# reading sum of elements between tab[x] and tab[y] in O(1) - thanks to prefix sum
def get_sum(tab, x, y):
    if x == 0:
        return tab[y]
    return tab[y] - tab[x-1]


def opt_sum(tab):
    n = len(tab)
    prefix_sum(tab)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]
    # basic cases
    for x in range(n-1):
        dp[x][x+1] = abs(get_sum(tab, x, x+1))
    # pure dynamic programming here
    for x in range(2, n):
        index1, index2 = 0, x
        while index2 < n:
            value = float("inf")
            for k in range(index1+1, index2-1):
                value = min(value, max(dp[index1][k], dp[k+1][index2]))
            value = min(value, max(abs(get_sum(tab, index1, index2)), min(dp[index1][index2-1], dp[index1+1][index2])))
            dp[index1][index2] = value
            index1 += 1
            index2 += 1
    return dp[0][-1]


tab = [-999, -1000, 1001, 1000]
print(opt_sum(tab))
