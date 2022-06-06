# Firstly, we add to given graph two vertices (super-source and super-sink). Now we can run Edmonds-Karp algorithm to
# count maximum flow and what is more important modify given structure to get a residual graph. At the end, we look at
# residual graph and check if there is no edge towards super-sink. If so, it means that flow along edges to the shops
# is maximum.

from math import inf
from collections import deque


def bfs(graph, parent, s, t):
    n = len(graph)
    visited = [0]*n
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


def edmonds_karp_algorithm(graph, s, t):
    n = len(graph)
    parent = [-1]*n
    max_flow = 0
    while bfs(graph, parent, s, t):
        flow = inf
        v = t
        while v != s:
            flow = min(flow, graph[parent[v]][v])
            v = parent[v]
        v = t
        max_flow += flow
        while v != s:
            graph[parent[v]][v] -= flow
            graph[v][parent[v]] += flow
            v = parent[v]
    return max_flow


def ex01(graph):
    n = len(graph)
    for x in range(n):
        graph[x].append(0)
        graph[x].append(0)
    n = len(graph[0])
    graph.append([0 for _ in range(n)])
    graph.append([0 for _ in range(n)])
    for x, y in factories:
        graph[n-2][x] = y
    for x, y in shops:
        graph[x][n-1] = y
    edmonds_karp_algorithm(graph, n-2, n-1)
    # here we look at residual graph and check whether all edges turned direction to opposite
    # and previous edge weight remained the same
    for x, y in shops:
        if graph[n-1][x] != y:
            return False
    return True


graph = [[0, 10, 0, 8, 0, 0, 0],
         [0, 0, 11, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 0],
         [0, 5, 0, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 12],
         [0, 0, 0, 0, 11, 0, 6],
         [0, 0, 0, 0, 0, 0, 0]]
factories = [(1, 12), (0, 9)]
shops = [(4, 4), (6, 6)]
print(ex01(graph))
