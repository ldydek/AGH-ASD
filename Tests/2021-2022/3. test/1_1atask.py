# At the beginning, we can change graph representation to more convenient (adjacency matrix). Now we can run simple
# Dijkstra's algorithm, but with linear searching for next vertex to consider (without priority queue). Additionally, if
# considering planet is special (has an ability to travel to other special planets with zero time) we don't do edge
# relaxation but just simply rewrite shortest time from considering planet.
# Time complexity: O(n^2)
# Space complexity: O(n)
# Passed all tests
# Time for all tests: ~3s

from kol3atesty import runtests


# O(m) - creating adjacency matrix
# m - edge list length
def create_graph(E, n):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for x, y, z in E:
        graph[x][y] = z
        graph[y][x] = z
    return graph


# O(n) - choosing next vertex to make edge relaxations
def choose_vertex(distance, visited):
    index, value = None, float("inf")
    for x in range(len(distance)):
        if distance[x] < value and visited[x] == 0:
            value = distance[x]
            index = x
    return index


# O(1) - edge relaxation
def relax(distance, graph, x, vertex):
    if distance[x] > distance[vertex] + graph[vertex][x]:
        distance[x] = distance[vertex] + graph[vertex][x]


def spacetravel(n, E, S, a, b):
    graph = create_graph(E, n)
    distance = [float("inf")] * n
    visited = [0] * n
    distance[a] = 0
    area = [0] * n
    for x in S:
        area[x] = 1

    while True:
        vertex = choose_vertex(distance, visited)
        if vertex is None:
            return
        visited[vertex] = 1
        if vertex == b:
            return distance[vertex]
        for x in range(n):
            # if there is an edge do the relaxation
            if graph[vertex][x] > 0:
                relax(distance, graph, x, vertex)
        # additionally if this planet is special we can get to other special planets in zero time
        if area[vertex] == 1:
            for x in S:
                distance[x] = distance[vertex]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
