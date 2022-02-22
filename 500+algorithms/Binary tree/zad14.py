# Znajdowanie następnego węzła w drzewie na tym samym poziomie drzewa (a więc pierwszego po prawej). Niekoniecznie jest
# to następnik!


class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None


def same_level(a, e):
    def reku(a, level=0):
        nonlocal level1
        if a is not None:
            zz = a.value
        if a is None:
            return
        if a == e:
            level1 = level
            return
        if level == level1:
            return a.value
        xd1 = reku(a.left, level+1)
        if xd1 is not None:
            return xd1
        xd2 = reku(a.right, level+1)
        if xd2 is not None:
            return xd2
    level1 = -1
    return reku(a)


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
print(same_level(a, g))
