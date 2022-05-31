# Idea is to determine given graph diameter, so the longest possible path in it between certain pair of vertices. We can
# do it by using two times BFS. Firstly, from random vertex and later from the furthest vertex which was shows by first
# BFS (it works only in a tree!). At the end, using "parent" array we can construct this diameter and travel only half
# of its length.
# Time complexity: O(V+E)
# Space complexity: O(V)
# Passed all tests
from collections import deque
from math import inf


# classical bfs implementation
def bfs(graph, queue, distance, parent, x):
    queue.append(x)
    distance[x] = 0
    while queue:
        u = queue.popleft()
        for i in range(len(graph[u])):
            if distance[graph[u][i]] == inf:
                distance[graph[u][i]] = distance[u] + 1
                parent[graph[u][i]] = u
                queue.append(graph[u][i])


# travelling half of the diameter
def choose_vertex(parent, distance, b):
    diameter_length = distance[b]
    for x in range(diameter_length//2):
        b = parent[b]
    return b


def best_root(L):
    n = len(L)
    queue = deque()
    distance = [inf] * n
    parent = [-1] * n
    bfs(L, queue, distance, parent, 0)
    vertex = 0
    # determine an appropriate vertex after first BFS
    for x in range(n):
        if distance[x] > distance[vertex]:
            vertex = x
    for x in range(n):
        parent[x] = -1
        distance[x] = inf
    bfs(L, queue, distance, parent, vertex)
    vertex = 0
    for x in range(n):
        if distance[x] > distance[vertex]:
            vertex = x
    # now after second BFS we know diameter length as well as where it exactly is
    # ("parent" array)
    return choose_vertex(parent, distance, vertex)


L = [[2], [2], [0, 1, 3], [2, 4], [3, 5, 6], [4], [4]]
print(best_root(L))
