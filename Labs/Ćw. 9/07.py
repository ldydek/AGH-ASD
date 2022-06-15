# We consider each graph vertex "D" times according to amount of fuel. We are in certain vertex (let's call it "v") and
# we have two options: either we fuel more (if it's possible) or we can try to move further. Only during fueling we add
# more to the distance, because this time we look not for shortest path but the cheapest one, so moving further doesn't
# cost us anything. We add to the priority queue tuples: (cost, vertex, fuel amount). Thanks to it we know if we can
# fuel more and which vertices are accessible for this state. If we pop from the queue the destination it means that
# the cheapest path is already correctly computed.

from math import inf
from queue import PriorityQueue


def print_path(parent, B):
    solution = [B]
    a, b = B, 0
    while parent[a][b] != (-1, -1):
        if parent[a][b][0] != a:
            solution.append(parent[a][b][0])
        a, b = parent[a][b]
    return solution[::-1]


def ex07(graph, costs, D, A, B):
    n = len(graph)
    distance = [[inf for _ in range(D+1)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(D+1)] for _ in range(n)]
    distance[A][0] = 0
    queue = PriorityQueue()
    queue.put((0, A, 0))

    while not queue.empty():
        c, v, f = queue.get()
        if v == B:
            return print_path(parent, B)

        if f != D:
            if distance[v][f+1] > distance[v][f] + costs[v]:
                distance[v][f+1] = distance[v][f] + costs[v]
                queue.put((distance[v][f+1], v, f+1))
                parent[v][f+1] = (v, f)

        for x, y in graph[v]:
            if y <= f:
                if distance[x][f-y] > distance[v][f]:
                    distance[x][f-y] = distance[v][f]
                    queue.put((distance[x][f-y], x, f-y))
                    parent[x][f-y] = (v, f)


graph = [[(1, 20), (4, 15)],
         [(0, 20), (3, 11), (2, 10)],
         [(1, 10), (5, 8)],
         [(1, 11), (4, 21), (5, 16)],
         [(0, 15), (3, 21), (5, 30)],
         [(2, 8), (3, 16), (4, 30)]]
costs = [20, 70, 100, 5, 50]
print(ex07(graph, costs, 20, 0, 5))
