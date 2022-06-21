# 1) At first, we can notice that tree is a bipartite graph. We traverse it using BFS/DFS marking vertices with 0/1
# values. Later, these ones with 0 will go to one set and the others ones to the second set. Now we can find matching
# with the biggest quantity using maximum flow algorithms (we can do it on bipartite graphs).
# Time complexity: O(VE) solution
# Space complexity: O(V^2)
# 2) Another approach to this problem is faster. We can use dynamic programming on tree to solve this problem using two
# functions: maximum matching including current node or excluding. Let "f" be the function describing including node and
# "g" excluding. Now we have recursions: f(v) = max(max(f(u),g(w)+1), where "u" and "w" are "v" children,
# g(v) = sum of f(u), where "u" is "v" children. At the end we choose max(f(root), g(root)).
# Time complexity: O(V+E)
# Space complexity: O(V)

# O(VE) implementation
from collections import deque
from math import inf


def bfs(graph, parent, s, t):
    n = len(graph)
    visited = [0] * n
    Q = deque()
    Q.append(s)
    visited[s] = 1
    while Q:
        u = Q.popleft()
        for x in range(n):
            if graph[u][x] != 0 and visited[x] == 0:
                visited[x] = 1
                parent[x] = u
                if x == t:
                    return True
                Q.append(x)


# O(VE) - in bipartite graphs
def edmonds_karp_algorithm(graph, s, t):
    n = len(graph)
    parent = [-1]*n
    max_flow = 0
    while bfs(graph, parent, s, t):
        v = t
        max_flow += 1
        while v != s:
            graph[parent[v]][v] -= 1
            graph[v][parent[v]] += 1
            v = parent[v]
    return max_flow


# traversing given tree using DFS to colour visiting vertices
# O(V+E) = O(V)
def dfs(graph, visited, v):
    for x in graph[v]:
        if visited[x] is None:
            visited[x] = 1 - visited[v]
            dfs(graph, visited, x)


# creating bipartite graph with two additional vertices: source and sink
# O(V^2)
def create_graph(visited):
    n = len(visited)
    graph = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for x in range(n):
        for y in range(n):
            if x == y:
                continue
            if visited[x] != visited[y]:
                graph[x][y] = 1
        if visited[x] == 0:
            graph[n][x] = 1
            graph[x][n] = 1
        else:
            graph[n+1][x] = 1
            graph[x][n+1] = 1
    return graph


def ex04_b(tree):
    n = len(tree)
    visited = [None] * n
    visited[0] = 0
    dfs(tree, visited, 0)
    graph = create_graph(visited)
    return edmonds_karp_algorithm(graph, n, n+1)


tree = [[1, 4, 6],
        [0, 2, 3],
        [1],
        [1],
        [0, 5],
        [4],
        [0, 7, 8, 9, 10],
        [6],
        [6],
        [6],
        [6]]


# O(V+E) implementation
class Node:
    def __init__(self):
        self.value = None
        self.children = []
        self.f = 0
        self.g = 0


# f - including node
# g - excluding node
def ex04_g(v):
    if len(v.children) == 0:
        v.g = 0
        v.f = 0
        return 0, 0
    if v.g != 0:
        return v.g
    if v.f != 0:
        return v.f
    for x in v.children:
        v.g += ex04_g(x)[0]
    value1, value2 = 0, 0
    node = None
    for x in v.children:
        value2 += x.f
        if value1 <= x.g:
            value1 = x.g
            node = x
    value2 -= node.f
    v.f = max(value1, value2) + 1
    return v.f, v.g


def create_tree():
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
    k = Node()
    a.value = 0
    b.value = 1
    c.value = 2
    d.value = 3
    e.value = 4
    f.value = 5
    g.value = 6
    h.value = 7
    i.value = 8
    j.value = 9
    k.value = 10
    a.children = [b, e, g]
    b.children = [c, d]
    e.children = [f]
    g.children = [h, i, j, k]
    return a


a = create_tree()
print(ex04_b(tree))
print(max(ex04_g(a)))
