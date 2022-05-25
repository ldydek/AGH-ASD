# Dijkstra's algorithm implementation on a graph given by adjacency matrix. Note that in this case we don't need to
# allocate heap (priority queue). Here, we can linearly traverse "distance" array and choose an appropriate unvisited
# vertex (for it shorted path isn't already computed). Later because of graph representation we have to traverse
# linearly again one of the matrix rows.

from math import inf


def choose_next_vertex(distance, visited):
    index, value = None, inf
    for x in range(len(distance)):
        if visited[x] == 0 and distance[x] < value:
            value = distance[x]
            index = x
    if index is None:
        return False
    visited[index] = 1
    return index


def relax(graph, distance, x, vertex):
    if distance[x] > distance[vertex] + graph[vertex][x]:
        distance[x] = distance[vertex] + graph[vertex][x]


def dijkstra_algorithm(graph, source):
    n = len(graph)
    visited = [0] * n
    distance = [inf] * n
    distance[source] = 0

    while True:
        vertex = choose_next_vertex(distance, visited)
        if vertex is False:
            return distance
        for x in range(n):
            if graph[vertex][x] > 0 and visited[x] == 0:
                relax(graph, distance, x, vertex)


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
print(dijkstra_algorithm(graph, 0))
