# Program tworzący drzewo BST z tablicy kluczy za pomocą wywołań funkcji insert. Nowy klucz jest do drzewa wstawiany
# na podstawie przyjętych warunków struktury drzewa BST (mniejsze na lewo, większe na prawo).


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def insert(root, key):
    x = Node(key)
    while root is not None:
        if root.key == x.key:
            return False
        elif root.key < x.key:
            if root.right is None:
                root.right = x
                x.parent = root
                # print("na prawo")
                return True
            else:
                root = root.right
                # print("na prawo", end=" ")
        else:
            if root.left is None:
                root.left = x
                x.parent = root
                # print("na lewo")
                return True
            else:
                root = root.left
                # print("na lewo", end=" ")


def tree_minimum(root):
    while root.left is not None:
        root = root.left
    return root


def tree_maximum(root):
    while root.right is not None:
        root = root.right
    return root


def successor(root, x):
    y = find(root, x)
    if y.right is not None:
        return tree_minimum(y.right)
    z = y.parent
    while z is not None and y == z.right:
        y = z
        z = z.parent
    return z


def find(root, x):
    while root is not None:
        if x < root.key:
            root = root.left
        elif x > root.key:
            root = root.right
        else:
            return root
    return False


def remove(root, x):
    while root is not None and x != root.key:
        if x < root.key:
            root = root.left
        elif x > root.key:
            root = root.right
    if root is None:
        return False
    # jeśli x nie ma synów, to po prostu usuwamy go, zastępując w jego ojcu wskaźnik na None
    if root.right is None and root.left is None:
        root.parent = None
    # jeśli x ma tylko jednego syna, to "podciągamy" tego syna na pozycję x, zastępując w ojcu
    # wskaźnik do x wskaźnikiem do syna x
    elif root.right is not None and root.left is None:
        root.parent = root.right
    elif root.left is not None and root.right is None:
        root.parent = root.left
    elif not root.right and not root.left:
        y = successor(root, x)
        if root.right == y:
            root.parent = y.right
        else:
            root.parent = root.right
            x.parent = root
    return True


def fun(a):
    def preorder_traversal(a):
        zz = a.value
        if a.left is not None:
            preorder_traversal(a.left)
        if a.right is not None:
            preorder_traversal(a.right)

    def inorder_traversal(a):
        if a.left is not None:
            inorder_traversal(a.left)
        zz = a.value
        if a.right is not None:
            inorder_traversal(a.right)

    def postorder_traversal(a):
        if a.left is not None:
            postorder_traversal(a.left)
        if a.right is not None:
            postorder_traversal(a.right)
        zz = a.value

    preorder_traversal(a)
    inorder_traversal(a)
    postorder_traversal(a)


root = Node(15)
tab = [20, 17, 16, 4, 10, 8, 19]
for x in range(len(tab)):
    insert(root, tab[x])
print(remove(root, 16))
