# Small modification of Dijkstra's algorithm. This time I add to the priority queue tuples: (distance from source,
# vertex, edge weight I travelled to this vertex). Thanks to it I know to which vertices I can travel and which ones
# to ignore. If I pop from queue destination point I am sure that minimum distance is correctly computed.
# Time complexity: O(E log V)
# Space complexity: O(V)
# Passed all tests

from math import inf
from queue import PriorityQueue


def relax(graph, distance, queue, v, x, w):
    if distance[change(graph[v][x])][x] > distance[change(w)][v] + graph[v][x]:
        distance[change(graph[v][x])][x] = distance[change(w)][v] + graph[v][x]
        queue.put((distance[change(graph[v][x])][x], x, graph[v][x]))


def change(w):
    if w == 5:
        return 1
    elif w == 8:
        return 2
    else:
        return 0


def islands(G1, A, B):
    n = len(G1)
    distance = [[inf for _ in range(n)] for _ in range(3)]
    for x in range(3):
        distance[x][A] = 0
    queue = PriorityQueue()
    queue.put((0, A, 0))

    while not queue.empty():
        d, v, w = queue.get()
        if v == B:
            return d
        for x in range(n):
            if G1[v][x] > 0 and G1[v][x] != w:
                relax(G1, distance, queue, v, x, w)


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]
print(islands(G1, 5, 2))
