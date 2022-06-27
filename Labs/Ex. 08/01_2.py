# Idea is to run BFS several times or more, but not on the entire graph but only on the part of it. If we run BFS from
# a certain vertex all vertices accessible from it will be marked as visited and only these accessible ones. So we come
# to the conclusion that one BFS will count one connected component. We run algorithm until all vertices are found.
# We visit each vertex only once so total time complexity is still O(V+E).

from collections import deque


def bfs(graph, distance, u, queue):
    queue.append(u)
    distance[u] = 1
    while queue:
        u = queue.popleft()
        for x in range(len(graph[u])):
            if distance[graph[u][x]] is None:
                distance[graph[u][x]] = 1
                queue.append(graph[u][x])


def ex02(graph):
    n = len(graph)
    distance = [None] * n
    queue = deque()
    ctr = 0
    for x in range(n):
        if distance[x] is None:
            ctr += 1
            bfs(graph, distance, x, queue)
    return ctr


graph = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1, 5], [4, 7], [7], [5, 6], [9], [8], [10]]
print(ex02(graph))
