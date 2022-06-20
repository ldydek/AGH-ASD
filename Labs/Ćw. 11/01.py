# We can easily modify given undirected graph to directed one which satisfies all flow network conditions. So for edge
# (u, v) we leave for instance direction (u, v) without changing and for direction (v, u) we remove that arch and create
# two ones (v, w) and (w, u), where "w" is an additional created vertex. All edge weights remain the same. We do that
# with every edge and at the and we have finally well-prepared flow network and we cun run Edmonds-Karp algorithm.
# Alternatively, we can notice that given undirected graph is a residual graph, so we can simply run maximum flow
# algorithm on it and start counting maximum flow from this stage (it means that if we run maximum flow algorithm on
# a directed graph there is a chance that we obtain residual graph which will be the same as undirected one as
# an input). So we come to the conclusion that if we start count maximum flow on the undirected graph we'll also get
# correct quantity at the end.

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


def edge_quantity(graph):
    n = len(graph)
    ctr = 0
    for x in range(n):
        for y in range(x+1, n):
            if graph[x][y] > 0:
                ctr += 1
    return ctr


def modify_new_graph(graph, new_graph):
    vertex = len(graph)
    n = vertex
    for x in range(n):
        for y in range(x+1, n):
            if graph[x][y] > 0:
                new_graph[x][y] = graph[x][y]
                new_graph[y][vertex] = new_graph[vertex][x] = graph[x][y]
                vertex += 1


def ex01(graph):
    n = len(graph)
    edges = edge_quantity(graph)
    new_graph = [[0 for _ in range(n + edges)] for _ in range(n + edges)]
    modify_new_graph(graph, new_graph)
    return edmonds_karp_algorithm(new_graph, 0, len(new_graph)-1)


graph = [[0, 8, 7, 5, 0],
         [8, 0, 0, 3, 0],
         [7, 0, 0, 5, 4],
         [5, 3, 5, 0, 8],
         [0, 0, 4, 8, 0]]
print(ex01(graph))
