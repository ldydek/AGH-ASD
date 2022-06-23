# At first, we change graph representation to adjacency list. Later we create a cycle between all special planets, so
# number of graph edges will increase maximally n-1, where "n" is a quantity of planets. On that graph we can run
# Dijkstra's algorithm and compute shortest path between "a" and "b".
# Time complexity: O((m+n) log n) - O(m+n) - entire number of edges
# but O((m+n) log n) = O(m log n)
# Space complexity: O(V)
# Passed all tests
# Time for all tests: ~ 0.06s

from kol3atesty import runtests
from queue import PriorityQueue
from math import inf


# O(m) - creating a graph from edge list
# m - number of edges
def create_graph(E, n):
    graph = [[] for _ in range(n)]
    for x, y, z in E:
        graph[x].append((y, z))
        graph[y].append((x, z))
    return graph


# O(n) - adding cycle between all special planets
def add_cycle(graph, S):
    n = len(S)
    for x in range(1, n):
        graph[S[x-1]].append((S[x], 0))
        graph[S[x]].append((S[x-1], 0))
    graph[S[0]].append((S[n-1], 0))
    graph[S[n-1]].append((S[0], 0))


# O(1)
def relax(queue, distance, x, v, y):
    if distance[x] > distance[v] + y:
        distance[x] = distance[v] + y
        queue.put((distance[x], x))


# O(m log n) - basic Dijkstra's algorithm implementation on lists
def dijkstra(graph, a, b):
    n = len(graph)
    distance = [inf] * n
    distance[a] = 0
    queue = PriorityQueue()
    queue.put((0, a))

    while not queue.empty():
        d, v = queue.get()
        if v == b:
            return d
        for x, y in graph[v]:
            relax(queue, distance, x, v, y)
    return


# O(m log n)
def spacetravel(n, E, S, a, b):
    graph = create_graph(E, n)
    add_cycle(graph, S)
    return dijkstra(graph, a, b)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
