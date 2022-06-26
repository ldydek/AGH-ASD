# Algorithm for finding BST successor of "x", where "x" is a certain BST node (element with a smallest value greater
# than "x"). We have here to cases: if "x" has a right child the successor will be a node with a minimum value in
# a subtree rooted in right child of "x". Otherwise, we are forced to move upwards until we find an element for which
# left child was last considered node. If that element doesn't exist it means that "x" doesn't have successor.
# Time complexity: O(h), where "h" is a BST height
# Space complexity: O(1)


def tree_minimum(root):
    while root.left is not None:
        root = root.left
    return root


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y
