# Firstly, we run Floyd-Warshall algorithm do determine shortest paths between all pairs of vertices. We have to do it
# to determine later if certain distance isn't smaller than "d". Now we have to find a path not necessarily shortest
# so basic queue will be sufficient here. We add to it tuples (x, y), where "x" and "y" are current drivers places.
# If we want to add to the queue tuple (y, x), where "x" and "y" are now starting positions it means that a path was
# eventually found. Thanks to "parent" matrix we can easily construct it.
# Time complexity: O(V^3)
# Space complexity: O(V^2)
# Passed all tests
from math import inf
from collections import deque


# basic Floyd-Warshall algorithm implementation
def floyd_warshall(M):
    n = len(M)
    distance = [[inf for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u == v:
                distance[u][v] = 0
                continue
            if M[u][v] > 0:
                distance[u][v] = M[u][v]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if distance[u][v] > distance[u][k] + distance[k][v]:
                    distance[u][v] = distance[u][k] + distance[k][v]
    return distance


# function constructing a path
def print_path(parent, a, b):
    solution = []
    while (a, b) != (-1, -1):
        solution.append((a, b))
        a, b = parent[a][b]
    return solution[::-1]


def keep_distance(M, x, y, d):
    n = len(M)
    distance = floyd_warshall(M)
    parent = [[(-1, -1) for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()

        # one of drivers stays
        for i in range(n):
            if M[a][i] > 0 and distance[b][i] >= d and visited[i][b] == 0:
                visited[i][b] = 1
                parent[i][b] = (a, b)
                queue.append((i, b))
                if (i, b) == (y, x):
                    return print_path(parent, i, b)
        for i in range(n):
            if M[b][i] > 0 and distance[a][i] >= d and visited[a][i] == 0:
                visited[a][i] = 1
                parent[a][i] = (a, b)
                queue.append((a, i))
                if (a, i) == (y, x):
                    return print_path(parent, a, i)

        # both of them are travelling
        for i in range(n):
            if M[a][i] > 0:
                for j in range(n):
                    # condition (a,b) != (j, i) means not travelling same edge 
                    if M[b][j] > 0 and distance[i][j] >= d and visited[i][j] == 0 and (a, b) != (j, i):
                        visited[i][j] = 1
                        parent[i][j] = (a, b)
                        queue.append((i, j))
                        if (i, j) == (y, x):
                            return print_path(parent, i, j)


M = [[0, 5, 1, 0, 0, 0],
     [5, 0, 0, 5, 0, 0],
     [1, 0, 0, 1, 0, 0],
     [0, 5, 1, 0, 1, 0],
     [0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 1, 0]]
x = 0
y = 5
d = 4
print(keep_distance(M, x, y, d))
