# Finding BST element with minimum and maximum value is quite easy. We have to just traverse BST constantly to the left
# for finding minimum and to the right for finding maximum. If we get to certain node that doesn't have left child it 
# means that we found minimum (same happens for finding maximum with right child).

def tree_minimum(root):
    while root.left is not None:
        root = root.left
    return root


def tree_maximum(root):
    while root.right is not None:
        root = root.right
    return root
