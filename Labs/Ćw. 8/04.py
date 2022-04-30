# Small modification of BFS algorithm, because this time we add to the queue tuples:
# (vertex; weight of edge we go to it). So when we delete this tuple, we know, thanks to second element, to which
# vertices we can go and which ones to ignore.

from collections import deque
from math import inf


def ex04(graph, x, y):
    queue = deque()
    queue.append((x, inf))
    while queue:
        a, b = queue.popleft()
        for i in range(len(graph)):
            if 0 < graph[a][i] < b:
                if i == y:
                    return True
                queue.append((i, graph[a][i]))
    return False


graph = [[0, 33, 15, 5, 31, 0, 0, 0],
         [33, 0, 1, 0, 0, 0, 0, 0],
         [15, 1, 0, 20, 0, 0, 0, 0],
         [5, 0, 20, 0, 0, 15, 10, 0],
         [31, 0, 0, 0, 0, 30, 0, 180],
         [0, 0, 0, 15, 30, 0, 21, 1],
         [0, 0, 0, 10, 0, 21, 0, 150],
         [0, 0, 0, 0, 180, 30, 15, 0]]
print(ex04(graph, 0, 7))
