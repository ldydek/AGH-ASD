# Program znajdujący wszystkich przodków danego węzła w drzewie.

class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None


def ancestors(a, k):
    def reku(a):
        if a is None:
            return
        if a.value == k:
            return k
        xd = reku(a.left)
        if xd:
            set.append(a.value)
            return xd
        xd = reku(a.right)
        if xd:
            set.append(a.value)
            return xd
    set = []
    reku(a)
    return set


a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
f = Node()
g = Node()
h = Node()
i = Node()
a.value = 1
b.value = 2
c.value = 3
d.value = 4
e.value = 5
f.value = 6
g.value = 7
h.value = 8
i.value = 9
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
f.left = h
g.right = i
print(ancestors(a, 9))
