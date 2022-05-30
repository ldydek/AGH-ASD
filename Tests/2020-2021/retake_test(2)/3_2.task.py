# Idea is to run Dijkstra's algorithm twice from "s" and "t" vertices. We will receive two shortest path trees as
# a product of algorithm. Now we can follow shortest path from "t" to "s" and check by the way following condition:
# distance(s, x) + w(x, v) + distance(v, t) = distance(s, t), where w is a weight function on all graph edges, "v" is
# a certain vertex on a shortest path between "s" and "t" and "x" is its neighbour. Note that shortest path doesn't have
# to be unique.
# Time complexity: O(E log V)
# Space complexity: O(V^2)
# Passed all tests
from math import inf
from queue import PriorityQueue
from collections import deque


# edge relaxation in Dijkstra's algorithm
def relax(distance, queue, y, x, w):
    if distance[y] > distance[x] + w:
        distance[y] = distance[x] + w
        queue.put((distance[y], y))


# basic implementation of Dijkstra's algorithm
def dijkstra_algorithm(G, source):
    n = len(G)
    distance = [inf] * n
    distance[source] = 0
    queue = PriorityQueue()
    queue.put((0, source))

    while not queue.empty():
        w, v = queue.get()
        for a, b in G[v]:
            relax(distance, queue, a, v, b)
    return distance


# using queue data structure we move along shortest path between "s" and "t"
# in a queue we keep vertices and for them we have to consider all edges
def checking(G, distance_s, distance_t, s, t):
    n = len(G)
    queue = deque()
    queue.append(t)
    solution = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited2 = [0 for _ in range(n)]

    while queue:
        v = queue.popleft()
        for a, b in G[v]:
            # condition for checking if given edge lies on the shortest path
            if distance_s[a] + b + distance_t[v] == distance_t[s] and visited[v][a] == 0:
                visited[v][a] = 1
                solution += 1
                if visited2[a] == 0:
                    visited2[a] = 1
                    queue.append(a)
    return solution


def paths(G, s, t):
    distance_s = dijkstra_algorithm(G, s)
    distance_t = dijkstra_algorithm(G, t)
    if distance_s[t] == inf:
        return 0
    return checking(G, distance_s, distance_t, s, t)


G = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
     [(0, 1), (10, 9)],
     [(0, 2), (10, 8)],
     [(0, 3), (10, 7)],
     [(0, 4), (10, 6)],
     [(0, 5), (10, 5)],
     [(0, 6), (10, 4)],
     [(0, 7), (10, 3)],
     [(0, 8), (10, 2)],
     [(0, 9), (10, 1)],
     [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)],
     [(12, 3)],
     [(11, 3)]]
s = 0
t = 11
print(paths(G, s, t))
