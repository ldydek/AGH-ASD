# Dynamic programming approach in a tree
# f(i, j) = maximum value of "j" edges that create consistent tree rooted in a "i" node
# recursion: f(i, j) = max(f(i.left, j-1), f(i.right, j-1), f(i.left, j-k)+f(i.right, k)), where 0 <= k <= j-2
# third condition can happen only if j >= 2, because we use information computed before from both subtrees, so we have
# to use two edges more to get to these subtrees if they exist of course
# I store computed values for each node in a new allocated array in a.X field of size "k+1"
# Time complexity: O(nk^2)
# Space complexity: O(nk)
# Passed all tests
from math import inf


class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.X = None


def valuable_tree_reku(a, k, sol):
#   new node so we are force to allocate a new array to store solutions of subproblems
    if a.X is None:
        a.X = [-inf] * (k + 1)
        a.X[0] = 0
#   basic case - value of 0 edges has to be 0
    if a.left is None and a.right is None:
        return
#   tree leaf so we back
    if a.left:
        valuable_tree_reku(a.left, k, sol)
    if a.right:
        valuable_tree_reku(a.right, k, sol)
#   after visiting left and right subtree we can start computing values of subproblems
    for x in range(1, k+1):
        best = -inf
        if a.left:
            best = a.leftval + a.left.X[x-1]
        if a.right:
            best = max(best, a.rightval + a.right.X[x-1])
        if a.left and a.right:
            for y in range(x-1):
                best = max(best, a.left.X[y]+a.right.X[x-y-2]+a.leftval+a.rightval)
        a.X[x] = best
        if x == k:
            sol[0] = max(sol[0], best)
#    sol[0] will be storing best value of the final solution
#    it's convenient to store it in an one element array, becuase values of it are not changing with a recursion 


def valuableTree(a, k):
    sol = [-inf]
    valuable_tree_reku(a, k, sol)
    return sol[0]


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()
A.left = B
A.right = E
A.leftval = 1
A.rightval = 5
B.left = D
B.leftval = 6
B.right = C
B.rightval = 2
C.left = F
C.leftval = 8
C.right = G
C.rightval = 10
k = 3
print(valuableTree(A, k))
