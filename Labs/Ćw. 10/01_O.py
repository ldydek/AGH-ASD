# Idea is similar to Dijkstra's algorithm, but here we are forces to allocate "distance" matrix. We can approach this
# problem by splitting each vertex to |E| vertices (that's way "distance" matrix will be |V|x|E|). Field distance[x][y]
# will inform us about shortest path from source to "x" vertex and getting to it with edge weight "y". Thanks to it we
# know now which edges coming from "x" we can consider and which ones omit (path with decreasing edge weights).
# To the priority queue I add tuples: (distance from the source, vertex, edge weight).

from math import inf
from queue import PriorityQueue


# edge relaxation
def relax(graph, queue, distance, parent, i, v, w):
    if distance[i][graph[v][i]] > distance[v][w] + graph[v][i]:
        distance[i][graph[v][i]] = distance[v][w] + graph[v][i]
        queue.put((distance[i][graph[v][i]], i, graph[v][i]))
        parent[i][graph[v][i]] = (v, w)


# function finding index with the lowest value in a row distance[y]
# that index will help construct the solution
def find_index(distance, y):
    index = 0
    for x in range(len(distance[0])):
        if distance[y][x] < distance[y][index]:
            index = x
    return index


def ex01(graph, x, y, e):
    n = len(graph)
    e += 2
    distance = [[inf for _ in range(e)] for _ in range(n)]
    visited = [[0 for _ in range(e)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(e)] for _ in range(n)]
    for i in range(e):
        distance[x][i] = 0
        visited[x][i] = 1
    queue = PriorityQueue()
    queue.put((0, x, e-1))
    # to ease edge cases I suppose that edge coming to source has a weight |E|+1

    while not queue.empty():
        d, v, w = queue.get()
        if v == y:
            index = find_index(distance, y)
            return print_path(parent, y, index)
        for i in range(n):
            if w > graph[v][i] > 0:
                relax(graph, queue, distance, parent, i, v, w)


def print_path(parent, y, index):
    solution = []
    while (y, index) != (-1, -1):
        solution.append(y)
        y, index = parent[y][index]
    return solution[::-1]


graph = [[0, 8, 4, 0, 1, 0],
         [8, 0, 7, 0, 0, 0],
         [4, 7, 0, 5, 0, 6],
         [0, 0, 5, 0, 0, 3],
         [1, 0, 0, 0, 0, 2],
         [0, 0, 6, 3, 2, 0]]
print(ex01(graph, 0, 5, 8))
# program detects two paths - one has a weight 23 and second one 21
