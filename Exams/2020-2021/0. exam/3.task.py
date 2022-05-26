# Idea is to implement something similar to Dijkstra's algorithm. In this case we can consider each vertex twice,
# because we can get to it in two different ways - using two-mile boots or not. So we are forced to allocate 2d arrays:
# "distance" for keeping distances of shortest path and "visited" for checking if for certain vertex shortest path was
# already computed. Note that here using heap (priority queue) is not necessary, because traversing "distance" matrix
# for picking up next vertex takes O(n) time. The same time complexity we use later for traversing one of the graph
# matrix rows. We can finish algorithm when we choose from "distance" array the destination vertex.
# Time complexity: O(n^3)
# Space complexity: O(n)
# Passed all tests

from math import inf


# function which helps us to choose next vertex
# reminder: we will possibly choose certain vertex twice
def choose_next_vertex(distance, visited):
    vertex = None
    value = inf
    for x in range(2):
        for y in range(len(distance[0])):
            if visited[x][y] == 0 and distance[x][y] < value:
                value = distance[x][y]
                vertex = (x, y)
    if vertex:
        visited[vertex[0]][vertex[1]] = 1
    return vertex


# simple basic edge relaxation
def relax(graph, distance, x, vertex):
    mode, y = vertex
    if distance[0][x] > distance[mode][y] + graph[x][y]:
        distance[0][x] = distance[mode][y] + graph[x][y]


# another edge relaxation but this time using two-mile boots
def jump_relax(graph, distance, x, y, z):
    if distance[1][x] > distance[0][z] + max(graph[x][y], graph[y][z]):
        distance[1][x] = distance[0][z] + max(graph[x][y], graph[y][z])


def jumper(G, s, w):
    n = len(G)
    distance = [[inf for _ in range(n)] for _ in range(2)]
    visited = [[0 for _ in range(n)] for _ in range(2)]
    distance[0][s] = 0

    while True:
        vertex = choose_next_vertex(distance, visited)
        if vertex[1] == w:
            return distance[vertex[0]][vertex[1]]
        for x in range(n):
            if graph[vertex[1]][x] > 0 and visited[0][x] == 0:
                relax(G, distance, x, vertex)
        # this condition happens when we have an ability to use two-mile boots
        if vertex[0] == 0:
            for x in range(n):
                for y in range(n):
                    if G[vertex[1]][x] > 0 and G[x][y] > 0 and visited[1][y] == 0 and y != vertex[1]:
                        jump_relax(G, distance, y, x, vertex[1])


graph = [[0, 1, 0, 0, 0],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 7, 0],
         [0, 0, 7, 0, 8],
         [0, 0, 0, 8, 0]]
print(jumper(graph, 0, 4))
