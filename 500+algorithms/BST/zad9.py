# Program wyliczający "k-tą" co do wielkości liczbę w drzewie BST. Drzewo przechodzę w porządku inorder i zliczam ilość
# odwiedzonych po drodze kluczy. Jeśli odwiedzę ich już "k", to wartość tę zwracam do ojca w drzewie wywołań rekursji.


class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None


def fun(a, k):
    def inorder_traversal(a):
        nonlocal ctr
        if a.left is not None:
            xd = inorder_traversal(a.left)
            if xd is not None:
                return xd
        ctr += 1
        if ctr == k:
            return a.value
        if a.right is not None:
            xd = inorder_traversal(a.right)
            if xd is not None:
                return xd
    ctr = 0
    return inorder_traversal(a)


a = Node()
a.value = 20
b = Node()
c = Node()
d = Node()
e = Node()
b.value = 10
c.value = 30
d.value = 27
e.value = 40
a.left = b
a.right = c
c.left = d
c.right = e
f = Node()
f.value = 50
e.right = f
print(fun(a, 3))
