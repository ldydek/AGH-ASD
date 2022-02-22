# Program sprawdzający, czy podane drzewo binarne jest drzewem BST.

from math import inf


class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None


def fun(a):
    def if_bst_tree(a, min, max):
        if a is None:
            return True
        zz = a.value
        if min < a.value < max:
            return if_bst_tree(a.left, min, a.value) and if_bst_tree(a.right, a.value, max)
        return False
    min = -inf
    max = inf
    if if_bst_tree(a, min, max) is False:
        return False
    return True


a = Node()
a.value = 20
b = Node()
c = Node()
d = Node()
e = Node()
b.value = 10
c.value = 30
d.value = 25
e.value = 40
a.left = b
a.right = c
c.left = d
c.right = e
print(fun(a))
