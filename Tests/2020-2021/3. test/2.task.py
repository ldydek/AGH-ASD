# Idea is to traverse given BST tree recursively and count for each node minimum from node's value and sum of counted
# values before from left and right subtrees if they exist. If only one exists we suppose that the second value is 0,
# for instance T.left exists and T.right not. Tree root has to be considered differently, because in that case we don't
# include root's value but only counted values from left and right subtrees if they exist.
# Time complexity: O(n) - one BST tree traversal
# Space complexity: O(h) - where "h" is tree's height (recursion)
# Passed all tests

from math import inf


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def parent(a):
    if a.parent is None:
        return True
    return False


def leaf(a):
    if a.left is None and a.right is None:
        return True
    return False


def cutthetree_reku(T, value):
    if T is None:
        return 0
    if leaf(T):
        return value
    if parent(T):
        value = cutthetree_reku(T.left, value) + cutthetree_reku(T.right, value)
    else:
        value = min(T.value, cutthetree_reku(T.left, value) + cutthetree_reku(T.right, value))
    return value


def cutthetree(T):
    value = inf
    return cutthetree_reku(T, value)


a = BNode(10)
b = BNode(3)
c = BNode(15)
d = BNode(-1)
e = BNode(-5)
f = BNode(11)
g = BNode(17)
a.left = b
a.right = c
b.parent = a
b.left = d
d.parent = b
d.left = e
e.parent = d
c.parent = a
c.left = f
c.right = g
f.parent = c
g.parent = c
print(cutthetree(a))
