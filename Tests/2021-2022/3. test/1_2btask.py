# Here idea is just to simply add one more vertex to the graph. It represents airspace, so we create edges to the rest
# of graph vertices with weight equal to cost of taking off/landing at each airport. On that graph we run Dijkstra's
# algorithm which will compute shortest/cheapest path from "s" to "t".
# Time complexity: O(m log n), where "m" is number of edges and "n" number of vertices
# Space complexity: O(n)
# Passed all tests
# Time for all test: ~ 0.09s

from kol3btesty import runtests
from queue import PriorityQueue
from math import inf


# O(n) - adding new vertex representing airspace to the graph
def add_vertex(G, A):
    n = len(G)
    G.append([])
    for x in range(n):
        G[x].append((n, A[x]))
        G[n].append((x, A[x]))


# O(1) - edge relaxation
def relax(distance, queue, x, v, y):
    if distance[x] > distance[v] + y:
        distance[x] = distance[v] + y
        queue.put((distance[x], x))


# O(m log n) - basic Dijkstra's implementation
def dijkstra(G, s, t):
    n = len(G)
    distance = [inf] * n
    queue = PriorityQueue()
    distance[s] = 0
    queue.put((0, s))

    while True:
        d, v = queue.get()
        if v == t:
            return d
        for x, y in G[v]:
            relax(distance, queue, x, v, y)


# O(m log n) - main function
def airports(G, A, s, t):
    add_vertex(G, A)
    return dijkstra(G, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
