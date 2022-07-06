# Dynamic programming approach
# f(i, j, k) - minimum cost of constructing BST with elements from freq[i] to freq[j] and beginning level "k"
# recursion: f(i, j, k) = min(f(i, x, k+1) + f(x+2, j, k+1) + (k+1)*freq[x]) if j - i >= 1 and i <= k <= j-2
# later we compare temporary value with:
# f(i, j, k) = min(freq[i]*(k+1) + f(i+1, j, k+1), freq[j]*(k+1) + f(i, j-1, k+1))
# first equation happens when we consider certain element as root and there are also left and right subtrees
# second equation happens when one of the subtrees doesn't exist
# solution: f(0, n-1, 0)
# Time complexity: O(n^4)
# Space complexity: O(n^3)


def ex037(freq):
    n = len(freq)
    # node numbers
    # dp[tree_level][first_element][second_element]
    dp = [[[float("inf") for _ in range(n)] for _ in range(n)] for _ in range(n)]

    # basic cases
    for x in range(n):
        for y in range(n):
            dp[x][y][y] = (x + 1) * freq[y]

    # pure dynamic programming here
    # we fill each array level diagonally from top left to bottom right
    # note that in recursive equation we use computed values from lower BST levels
    # so in bottom-up approach we are forced to start from the lowest BST level and move upwards
    for bst_level in range(n-2, -1, -1):
        for x in range(1, n):
            index1, index2 = 0, x
            value = float("inf")
            while index2 < n:
                for k in range(index1, index2-1):
                    value = min(value, dp[bst_level+1][index1][k] + dp[bst_level+1][k+2][index2] + freq[k] * (bst_level + 1))
                value = min(value, freq[index1] * (bst_level + 1) + dp[bst_level+1][index1+1][index2])
                value = min(value, freq[index2] * (bst_level + 1) + dp[bst_level+1][index1][index2-1])
                dp[bst_level][index1][index2] = value
                index1 += 1
                index2 += 1
    return dp[0][0][-1]


freq = [25, 10, 20]
print(ex037(freq))
