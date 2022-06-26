# Functions for creating binary search tree from given array of values by adding to the BST tree new element. Idea for
# inserting new node is quite simple. We start from the root and move to the left or right depending on new element
# value. Entire time we keep additional pointer to the node that was visited by front pointer before. Now if front
# pointer is None, back pointer points to the leaf node for which we will be changing its class fields.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def insert(T, key):
    x = T
    y = None
    z = Node(key)
    # creating new node here
    while x is not None:
        y = x
        if x.key < z.key:
            x = x.right
        else:
            x = x.left
    z.parent = y
    # now parent of new element is "y" (leaf node)
    if y is None:
        return z
    # depending on "z" value we set new node as left or right child of "y"
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return T
    # at the end we return BST root


# function for checking if BST tree was successfully created
# after inorder tree traversal nodes values should be printed in the increasing order
def inorder_traversal(T):
    if T.left:
        inorder_traversal(T.left)
    print(T.key, end=" ")
    if T.right:
        inorder_traversal(T.right)


# creating binary search tree by several or more times inserting to it new element
def create_bst(tab):
    root = None
    for x in tab:
        root = insert(root, x)
    inorder_traversal(root)


tab = [10, 2, 13, 5, 7, 11, 1]
create_bst(tab)
