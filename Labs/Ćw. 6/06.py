# f(v) - length of the best path that starts in node "v" and heads towards leaves
# recursion: f(v) = max(f(v.children[k])) + v.value, where 0 <= k <= len(v.children)-1
# solution: max(f(k), f(m)+f(n)+k.value), where "k" is one of tree nodes and "m", "n" are its children
# case f(m)+f(n) will occur if both "m" and "n" nodes will be included in the best path
# edge case: f(v) = v.value, when "v" is a leaf
# note that considered tree doesn't have to be binary!
# Time complexity: O(v)
# Space complexity: O(h), where "h" is the height of a tree
from math import inf


class Node:
    def __init__(self):
        self.value = None
        self.children = []
        self.val = None


def ex06(a):
    sol = [-inf]
    ex06_recu(a, sol)
    return sol[0]


def ex06_recu(a, sol):
    if len(a.children) == 0:
        a.val = a.value
        sol[0] = max(sol[0], a.val)
        return a.value
    best, second_best = -inf, -inf
    for x in range(len(a.children)):
        best = max(best, ex06_recu(a.children[x], sol))
    a.val = best + a.value
    for x in range(len(a.children)):
        if a.children[x].val == best:
            continue
        second_best = max(second_best, a.children[x].value)
    sol[0] = max(sol[0], max(a.val, best+second_best+a.value))
    return a.val


a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
f = Node()
g = Node()
h = Node()
i = Node()
j = Node()
a.value = 10
b.value = -10
c.value = 2
d.value = 3
e.value = -2
f.value = 10
g.value = 20
h.value = 100
i.value = 80
j.value = 300
a.children.append(b)
b.children.append(c)
b.children.append(d)
d.children.append(e)
d.children.append(f)
a.children.append(g)
g.children.append(h)
g.children.append(i)
g.children.append(j)
print(ex06(a))
