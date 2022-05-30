# Idea is to change graph representation to adjacency matrix and run Floyd-Warshall algorithm to find shortest paths
# between all vertices. Now I can move from "t" vertex to "s" along the shortest path and by the way consider all
# neighbours on a shortest path of a certain vertex. Let's call it "v". Now if this condition happens:
# distance(s, x) + w(x, v) + distance(v, t) = distance(s, t) it means that edge (x, v) also is on the shortest path
# between "s" and "t" ("x" is one of "v" neighbours). Note that shortest path doesn't have to be unique.
# Time complexity: O(V^3)
# Space complexity: O(v^2)
# Passed all tests
from math import inf
from collections import deque


# basic implementation of floyd-warshall algorithm
def floyd_warshall_algorithm(graph):
    n = len(graph)
    distance = [[inf for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y:
                distance[x][y] = 0
                continue
            if graph[x][y] != 0:
                distance[x][y] = graph[x][y]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if distance[u][v] > distance[u][k] + distance[k][v]:
                    distance[u][v] = distance[u][k] + distance[k][v]
    return distance


# function that follows from "t" to "s" and checks by the way all neighbours on the shortest path
# of all vertices on it
def checking(distance, graph, s, t):
    n = len(distance)
    solution = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited2 = [0 for _ in range(n)]
    queue = deque()
    queue.append(t)

    while queue:
        v = queue.popleft()
        for x in range(n):
            if graph[v][x] != inf and visited[v][x] == 0:
                visited[v][x] = 1
                # condition that helps us determine if given edge lies on the shortest path
                if distance[s][x] + graph[v][x] + distance[v][t] == distance[s][t]:
                    solution += 1
                    if visited2[x] == 0:
                        visited2[x] = 1
                        queue.append(x)
    return solution


def paths(G, s, t):
    n = len(G)
    graph = [[inf for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y, z in G[x]:
            graph[x][y] = z
    distance = floyd_warshall_algorithm(graph)
    # if "s" and "t" are in two different connected components
    # simply return 0, because shortest path between them doesn't exist
    if distance[s][t] == inf:
        return 0
    return checking(distance, graph, s, t)


G = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
     [(0, 1), (10, 9)],
     [(0, 2), (10, 8)],
     [(0, 3), (10, 7)],
     [(0, 4), (10, 6)],
     [(0, 5), (10, 5)],
     [(0, 6), (10, 4)],
     [(0, 7), (10, 3)],
     [(0, 8), (10, 2)],
     [(0, 9), (10, 1)]
     [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)],
     [(12, 3)],
     [(11, 3)]]
s = 0
t = 11
print(paths(G, s, t))
