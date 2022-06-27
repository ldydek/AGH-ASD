# Classical BFS with "parent" array. Thanks to it we can construct shortest paths from the given source.

from math import inf
from collections import deque


def print_path(parent, s, t):
    solution = []
    while t != -1:
        solution.append(t)
        t = parent[t]
    return solution[::-1]


def bfs(tab, s, t):
    n = len(tab)
    distance = [None]*n
    parent = [inf]*n
    distance[s] = 0
    parent[s] = -1
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for x in range(len(tab[u])):
            if distance[tab[u][x]] is None:
                distance[tab[u][x]] = distance[u] + 1
                parent[tab[u][x]] = u
                Q.append(tab[u][x])
    return print_path(parent, s, t)


tab = [[1, 2], [0], [0, 3, 5], [2, 4, 5], [3], [2, 3]]
print(bfs(tab, 0, 4))
