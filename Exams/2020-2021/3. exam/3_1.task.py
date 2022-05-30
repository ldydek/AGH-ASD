# Idea is to allocate new binary array and if number of node is in a "C" array we can write on that index 1. Later, we
# traverse given binary tree recursively and thanks to additional array we can check in O(1) time if we should consider
# visited node and possibly change maximum value.
# Time complexity: O(n+m)
# Space complexity: O(n)
# Passed all tests

from zad3testy import runtests


# getting the number of right child if it exists
def right(i):
    return 2 * i + 1


# function which helps us determine number of nodes in a tree
# we use the fact that binary tree is full
# in this case it means that if it has height "h", it also has 2^(h+1) - 1 nodes
def get_n(T, el):
    while T.right:
        T = T.right
        el[0] = right(el[0])


# traversing the tree recursively
def traverse_the_tree(T, el, array, index):
    if array[index] == 1:
        el[0] = max(el[0], T.key)
    if T.left:
        traverse_the_tree(T.left, el, array, 2 * index)
    if T.right:
        traverse_the_tree(T.right, el, array, 2 * index + 1)


def maxim(T, C):
    el = [1]
    get_n(T, el)
    array = [0 for _ in range(el[0] + 1)]
    for x in range(len(C)):
        array[C[x]] = 1
    # now nodes that we are interested in have 1 value, rest of them 0
    el[0] = float("-inf")
    traverse_the_tree(T, el, array, 1)
    return el[0]


runtests(maxim)
