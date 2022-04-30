# In other words, we have to find order of deleting edges to maintain graph consistency. Two approaches using either
# BFS or DFS.

from collections import deque
from math import inf


# 1) BFS
def ex01_O_BFS(graph):
    n = len(graph)
    distance = [inf] * n
    order = [0]
    queue = deque()
    distance[0] = 0
    queue.append(0)
    while queue:
        u = queue.popleft()
        for x in range(len(graph[u])):
            if distance[graph[u][x]] == inf:
                distance[graph[u][x]] = distance[u] + 1
                queue.append(graph[u][x])
                order.append(graph[u][x])
    return order[::-1]


# 2) DFS
def ex01_O_DFS(graph):
    n = len(graph)
    visited = [0] * n
    visited[0] = 1
    order = []
    dfs_visit(graph, visited, order, 0)
    return order


def dfs_visit(graph, visited, order, x):
    for i in range(len(graph[x])):
        if visited[graph[x][i]] == 0:
            visited[graph[x][i]] = 1
            dfs_visit(graph, visited, order, graph[x][i])
    order.append(x)


graph = [[1, 2], [0, 2, 3, 4], [0, 1, 6, 7, 8], [1, 5], [1], [3], [2], [2], [9, 10], [8], [8]]
print(ex01_O_BFS(graph))
print(ex01_O_DFS(graph))
