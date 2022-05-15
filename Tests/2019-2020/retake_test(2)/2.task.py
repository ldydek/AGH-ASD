#


from math import inf
from queue import PriorityQueue


def relax(distance, queue, W, x, v, ctr):
    if distance[x[0]][ctr] > distance[v][ctr-1] + x[1]:
        distance[x[0]][ctr] = distance[v][ctr-1] + x[1]
        queue.put((distance[x[0]][ctr], W[ctr], x[0], ctr))


def dijkstra(graph, W, source, L):
    n = len(graph)
    distance = [[inf for _ in range(len(W))] for _ in range(n)]
    distance[source][0] = 0
    queue = PriorityQueue()
    ctr = 0
    queue.put((0, W[ctr], source, ctr))

    while not queue.empty():
        d, l, v, ctr = queue.get()
        if l == W[-1] and ctr == len(W)-1:
            return d
        ctr += 1
        for x in graph[v]:
            if W[ctr] == L[x[0]]:
                relax(distance, queue, W, x, v, ctr)


def letters(G, W):
    L, E = G
    vertices = 0
    for x in range(len(E)):
        vertices = max(vertices, E[x][0], E[x][1])
    vertices += 1
    graph = [[] for _ in range(vertices)]
    for x in E:
        graph[x[0]].append((x[1], x[2]))
        graph[x[1]].append((x[0], x[2]))
    graph.append([])
    for x in range(vertices):
        if L[x] == W[0]:
            graph[vertices].append((x, 0))
            graph[x].append((vertices, 0))
    source = vertices
    W = "a" + W
    L.append("a")
    return dijkstra(graph, W, source, L)


L = ['k', 'k', 'o', 'o', 't', 't', 'a', 'a', 'a']
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
G = (L, E)
W = "kokotok"
print(letters(G, W))
