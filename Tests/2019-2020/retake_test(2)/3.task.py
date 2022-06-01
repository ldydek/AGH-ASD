# Idea is to construct a graph of "n" vertices and if certain two numbers have a common digit we can create an edge
# (w, v) where "w" and "v" are indexes of these numbers in an array. On that graph we can run Dijkstra's algorithm,
# which will compute shortest path from the lowest to the biggest element.
# Time complexity: O(kn^2), where "k" is the word length
# Space complexity: O(n^2)
# Passed all tests
from math import inf


# checking whether given two numbers have common digit - O(k)
def digit(x, y):
    digits = [0] * 10
    while x:
        digits[x % 10] = 1
        x //= 10
    while y:
        if digits[y % 10] == 1:
            return True
        y //= 10
    return False


# creating graph as an adjacency matrix - O(kn^2)
def create_graph(T):
    n = len(T)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(x+1, n):
            if digit(T[x], T[y]):
                graph[x][y] = abs(T[x]-T[y])
                graph[y][x] = abs(T[x]-T[y])
    return graph


# finding minimum and maximum of the given array - O(n)
def find_min_max(T):
    n = len(T)
    index1, index2 = 0, 0
    for x in range(n):
        if T[x] < T[index1]:
            index1 = x
        elif T[x] > T[index2]:
            index2 = x
    return index1, index2


# finding next vertex to consider in Dijkstra's algorithm - O(n)
def find_index(distance, visited):
    n = len(distance)
    index, value = None, inf
    for x in range(n):
        if visited[x] == 0 and distance[x] < value:
            value = distance[x]
            index = x
    if index is not None:
        visited[index] = 1
    return index


# edge relaxation - O(1)
def relax(distance, graph, x, index):
    if distance[x] > distance[index] + graph[index][x]:
        distance[x] = distance[index] + graph[index][x]


# basic Dijkstra's algorithm implementation - O(n^2)
def dijkstra(graph, a, b):
    n = len(graph)
    distance = [inf] * n
    visited = [0] * n
    distance[a] = 0

    while True:
        index = find_index(distance, visited)
        if index is None:
            return -1
        elif index == b:
            return distance[b]
        for x in range(n):
            if graph[index][x] > 0 and visited[x] == 0:
                relax(distance, graph, x, index)


def cost(T):
    graph = create_graph(T)
    a, b = find_min_max(T)
    return dijkstra(graph, a, b)


T = [123, 890, 688, 587, 257, 246]
print(cost(T))
