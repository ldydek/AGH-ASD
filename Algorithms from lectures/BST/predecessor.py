# Algorithm for finding BST predecessor of "x", where "x" is a certain BST node (element with a greatest value smaller
# than "x"). We have here to cases: if "x" has a left child the successor will be a node with a maximum value in
# a subtree rooted in left child of "x". Otherwise, we are forced to move upwards until we find an element for which
# right child was last considered node. If that element doesn't exist it means that "x" doesn't have predecessor.
# Time complexity: O(h), where "h" is a BST height
# Space complexity: O(1)

def tree_maximum(root):
    while root.right is not None:
        root = root.right
    return root


def tree_predecessor(x):
    if x.left is not None:
        return tree_maximum(x.left)
    y = x.parent
    while y is not None and x == y.left:
        x = y
        y = y.parent
    return y
