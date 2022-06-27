# Idea is to from random vertex run BFS and gain shortest path tree (given graph is a weighted tree so each edge will
# be relaxed only once). Now we can run BFS once more from the furthest vertex (let's call it "v") as a root. After
# second BFS path from furthest vertex (let's call it "u") to "v" creates graph diameter. This idea with two BFS works
# only on trees! At the end, thanks to "parent" array we traverse diameter and find an appropriate vertex for which
# absolute value from distances to "u" and "v" is the lowest. That vertex is an answer.
# Time complexity: O(V) - BFS and diameter traversal (all O(V))
# Space complexity: OV)

from collections import deque
from math import inf


def relax(distance, parent, queue, x, v, y):
    if distance[x] > distance[v] + y:
        distance[x] = distance[v] + y
        parent[x] = v
        queue.append(x)


def bfs(graph, source):
    n = len(graph)
    queue = deque()
    distance = [inf] * n
    parent = [-1] * n
    distance[source] = 0
    queue.append(source)

    while queue:
        v = queue.popleft()
        for x, y in graph[v]:
            relax(distance, parent, queue, x, v, y)
    return distance, parent


def choose_vertex(distance):
    n = len(distance)
    index = 0
    for x in range(n):
        if distance[x] > distance[index]:
            index = x
    return index


def follow_diameter(distance, parent, index):
    vertex, value = None, inf
    v = index
    while index != -1:
        if abs(distance[parent[index]] - (distance[v] - distance[parent[index]])) < value:
            value = abs(distance[parent[index]] - (distance[v] - distance[parent[index]]))
            vertex = parent[index]
        index = parent[index]
    return vertex


def minimum_distance(graph):
    source = 0
    distance = bfs(graph, source)[0]
    index = choose_vertex(distance)
    distance, parent = bfs(graph, index)
    index = choose_vertex(distance)
    return follow_diameter(distance, parent, index)


graph = [[(1, 1)],
         [(0, 1), (2, 1), (4, 2)],
         [(1, 1), (3, 1)],
         [(2, 1)],
         [(1, 2), (5, 1), (8, 3)],
         [(4, 1), (6, 1)],
         [(5, 1), (7, 1)],
         [(6, 1)],
         [(4, 3), (9, 1), (11, 3), (12, 2)],
         [(8, 1), (10, 1)],
         [(9, 1)],
         [(8, 2)],
         [(8, 2), (13, 10), (16, 5)],
         [(12, 10), (14, 1)],
         [(13, 1), (15, 1)],
         [(14, 1)],
         [(12, 5), (17, 1)],
         [(16, 1), (18, 1)],
         [(17, 1)]]
print(minimum_distance(graph))
