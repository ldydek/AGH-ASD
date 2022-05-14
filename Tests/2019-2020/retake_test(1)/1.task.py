# Idea is to modify dijkstra's algorithm. This time we add to the priority queue tuples: (distance from source,
# vertex, amount of fuel after possible vehicle fueling). So in a "distance" matrix, for instance, distance[x][y] will
# inform us about temporary shortest path from the source to "x" vertex having "y" litres of fuel. Of course, when
# we meet a petrol station at point "x" it's always better to fuel the vehicle so in this case we just consider
# situation distance[x][d], where "d" is a capacity of a tank.
# Time complexity: O(nd log nd)
# Space complexity: O(nd)
# Passed all tests

from math import inf
from queue import PriorityQueue


def relax(queue, graph, petrol, distance, parent, x, y, f):
    d = len(distance[x])
    if petrol[x] == 1:
        if distance[x][d-1] > distance[y][f] + graph[y][x]:
            distance[x][d-1] = distance[y][f] + graph[y][x]
            parent[x][d-1] = (y, f)
            queue.put((distance[x][d-1], x, d-1))
    else:
        if distance[x][f-graph[y][x]] > distance[y][f] + graph[y][x]:
            distance[x][f-graph[y][x]] = distance[y][f] + graph[y][x]
            parent[x][f-graph[y][x]] = (y, f)
            queue.put((distance[x][f-graph[y][x]], x, f-graph[y][x]))


def find_index(distance):
    index = 0
    for x in range(len(distance)):
        if distance[x] < distance[index]:
            index = x
    return index


def print_path(parent, b, index):
    solution = []
    while (b, index) != (-1, -1):
        solution.append(b)
        b, index = parent[b][index]
    return solution[::-1]


def jak_dojade(G, P, d, a, b):
    n = len(G)
    distance = [[inf for _ in range(d+1)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(d+1)] for _ in range(n)]
    petrol = [0] * n
    queue = PriorityQueue()

    for x in range(len(P)):
        petrol[P[x]] = 1
    distance[a][d] = 0
    queue.put((0, a, d))

    while not queue.empty():
        d, v, f = queue.get()
        if v == b:
            index = find_index(distance[b])
            return print_path(parent, b, index)
        for y in range(n):
            if G[v][y] != -1 and f >= G[v][y]:
                relax(queue, G, petrol, distance, parent, y, v, f)
    return None


G = [[-1, 6, -1, 5, 2],
     [-1, -1, 1, 2, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 4, -1, -1],
     [-1, -1, 8, -1, -1]]
P = [0, 1, 3]
d = 6
a = 0
b = 2
print(jak_dojade(G, P, d, a, b))
