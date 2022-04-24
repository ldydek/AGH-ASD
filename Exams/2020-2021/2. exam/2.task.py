# f(v) - sum of all subtree edges rooted in "v" node
# Idea is to traverse given tree recursively and this sum keep in a new class field called v.sum. Later, I traverse
# the tree one more time, consider each node and count the difference between sum of all edges in a subtree rooted in
# one of its children and remaining part of the entire tree apart from this edge which was deleted.
# Time complexity: O(n)
# Passed all tests

from math import inf


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.sum = 0

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)


def traverse_the_tree(T):
    if len(T.edges) == 0:
        return T.sum
    for x in range(len(T.edges)):
        traverse_the_tree(T.edges[x])
        T.sum += T.weights[x] + T.edges[x].sum


def get_solution(T, solution, sum):
    if len(T.edges) == 0:
        return
    for x in range(len(T.edges)):
        if solution[0] > abs(T.edges[x].sum - (sum - T.edges[x].sum - T.weights[x])):
            solution[0] = abs(T.edges[x].sum - (sum - T.edges[x].sum - T.weights[x]))
            solution[1] = T.ids[x]
        get_solution(T.edges[x], solution, sum)


def balance(T):
    solution = [inf, None]
    traverse_the_tree(T)
    get_solution(T, solution, T.sum)
    return solution[1]


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()
H = Node()
A.addEdge(B, 583, 6)
A.addEdge(C, 154, 7)
B.addEdge(D, 623, 2)
D.addEdge(E, 651, 1)
B.addEdge(H, 508, 5)
H.addEdge(F, 373, 4)
F.addEdge(G, 513, 3)
print(balance(A))
