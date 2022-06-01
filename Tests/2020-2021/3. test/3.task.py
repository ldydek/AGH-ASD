# Firstly, we run Floyd-Warshall algorithm do compute distances between all pairs of vertices. Later we can construct
# directed bipartite graph. Edges in it will be only between vertices of different colours that lies in a distance
# greater or equal to "D" and will have weight 1. On that graph we can finally run Edmonds-Karp algorithm to compute
# maximal matching.
# Time complexity: O(n^3)
# Space complexity: O(n^2)
# Passed all tests

from math import inf
from collections import deque


# basic Floyd-Warshall implementation
def floyd_warshall_algorithm(tab):
    n = len(tab)
    distance = [[inf for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y:
                distance[x][y] = 0
            if tab[x][y] > 0:
                distance[x][y] = tab[x][y]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if distance[u][v] > distance[u][k] + distance[k][v]:
                    distance[u][v] = distance[u][k] + distance[k][v]
    return distance


# BFS to Edmonds-Karp
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


# constructing directed bipartite graph
def construct_graph(distance, K, D):
    n = len(distance)
    graph = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for x in range(n):
        for y in range(n):
            if distance[x][y] >= D and K[x] == "B" and K[y] == "G":
                graph[x][y] = 1
    for x in range(n):
        if K[x] == "B":
            graph[n][x] = 1
        elif K[x] == "G":
            graph[x][n+1] = 1
    return graph


def BlueAndGreen(T, K, D):
    n = len(T)
    distance = floyd_warshall_algorithm(T)
    graph = construct_graph(distance, K, D)
    return edmonds_karp_algorithm(graph, n, n+1)


T = [[0, 1, 1, 0, 1],
     [1, 0, 0, 1, 0],
     [1, 0, 0, 0, 1],
     [0, 1, 0, 0, 1],
     [1, 0, 1, 1, 0]]
K = ['B', 'B', 'G', 'G', 'B']
D = 2
print(BlueAndGreen(T, K, D))
