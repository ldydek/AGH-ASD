# Program wypisujący najwartościowszą ścieżkę od korzenia do pewnego liścia (jej wartość to suma odwiedzanych przez tę
# ścieżkę węzłów).


class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None


def valuable_path(a):
    if a is None:
        return 0
    xd = max(valuable_path(a.left), valuable_path(a.right)) + a.value
    return xd



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
i.value = 90
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
f.left = h
g.right = i
b.parent = a
c.parent = a
d.parent = b
e.parent = b
f.parent = c
g.parent = c
h.parent = f
i.parent = g
print(valuable_path(a))
