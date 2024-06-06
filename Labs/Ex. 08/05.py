from math import inf
from collections import deque


def bfs(graph, s, t):
    n = len(graph)
    queue = deque()
    distance = [inf] * n
    distance[s] = 0
    queue.append(s)

    while queue:
        x = queue.popleft()
        for v, w in graph[x]:
            if distance[v] > distance[x] + w:
                distance[v] = distance[x] + w

                if w:
                    queue.append(v)
                else:
                    queue.appendleft(v)

    return distance[t]


graph = [[(1, 0), (2, 1), (3, 1), (4, 1)], [(0, 0), (2, 0)], [(0, 1), (1, 0), (4, 0)], [(0, 1), (4, 1)], [(0, 1), (2, 0), (3, 1)]]
print(bfs(graph, 0, 4))
