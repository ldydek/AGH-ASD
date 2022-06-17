# We can construct a directed graph from given list (there will be a directed edge (u, v) if I[u][1] == I[v][0]). By the
# way we can omit these intervals which are not included fully in interval (x, y), because they will not be considered
# in a solution. Now we can run BFS/DFS algorithm twice from "x" and "y" vertices. This vertices which will be visited
# in both traversals are part of a solution.
# Time complexity: O(n^2)
# Space complexity: O(n)
# Passed all tests

from zad1testy import runtests
from collections import deque


def create_graph(I, a, b):
    n = len(I)
    n += 2
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n-2):
        for y in range(n-2):
            if I[x][1] == I[y][0] and a <= I[x][0] <= b and a <= I[y][1] <= b:
                graph[x][y] = 1
    for x in range(n-2):
        if I[x][0] == a:
            graph[n-2][x] = 1
        if I[x][1] == b:
            graph[x][n-1] = 1
    return graph


def transpose_graph(graph):
    n = len(graph)
    for x in range(n):
        for y in range(x, n):
            graph[x][y], graph[y][x] = graph[y][x], graph[x][y]


def bfs(graph, s):
    n = len(graph)
    queue = deque()
    queue.append(s)
    visited = [0] * n
    visited[s] = 1
    while queue:
        u = queue.popleft()
        for x in range(n):
            if graph[u][x] == 1 and visited[x] == 0:
                queue.append(x)
                visited[x] = 1
    return visited


def intuse(I, x, y):
    n = len(I)
    graph = create_graph(I, x, y)
    visited_x = bfs(graph, n)
    transpose_graph(graph)
    visited_y = bfs(graph, n+1)
    solution = []
    for i in range(n):
        if visited_x[i] == visited_y[i] == 1:
            solution.append(i)
    return solution


runtests(intuse)
