# Program znajdujący średnicę drzewa. Rekurencyjnie przechodzę drzewo i obliczam wysokość lewego i prawego dziecka
# dla danego węzła. Sumę tych wyników zapisuję w zmiennej nielokalnej a obliczone wysokości danych poddrzew przekazuję
# wyższym instancjom wywołań funkcji. Złożoność obliczeniowa: O(n).


class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None


def diameter(a):
    def reku(a):
        nonlocal solution
        if a is not None:
            zz = a.value
        if a.left is None and a.right is None:
            return 0
        elif a.left is not None and a.right is None:
            xd1 = reku(a.left)
            solution = max(solution, xd1+1)
            return xd1+1
        elif a.left is None and a.right is not None:
            xd2 = reku(a.right)
            solution = max(solution, xd2+1)
            return xd2+1
        elif a.left is not None and a.right is not None:
            xd1 = reku(a.left)
            solution = max(solution, xd1+1)
            xd2 = reku(a.right)
            solution = max(solution, xd2+1, xd1+xd2+2)
            return max(xd1, xd2)+1
    solution = 0
    reku(a)
    return solution


a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
f = Node()
g = Node()
a.value = 13
# b.value = 10
c.value = 20
# d.value = 13
e.value = 16
f.value = 23
g.value = 40
# a.left = b
a.right = c
# b.right = d
c.left = e
c.right = f
f.right = g
h = Node()
h.value = 11
d.left = h
i = Node()
i.value = 15
e.left = i
j = Node()
k = Node()
i.left = j
g.right = k
print(diameter(a))

