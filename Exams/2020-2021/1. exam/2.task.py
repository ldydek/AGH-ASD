# Passed all tests

from math import inf
from queue import PriorityQueue


def robot(L, A, B):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    distance = [[[[inf for _ in range(4)] for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]
    velocity = [0, 60, 40, 30]
    queue = PriorityQueue()
    queue.put((0, A, 1, 0))
    distance[A[1]][A[0]][1][0] = 0

    while not queue.empty():
        t, p, d, v = queue.get()
        if p == B:
            return t

        # turns
        if distance[p[1]][p[0]][(d+1) % 4][0] > distance[p[1]][p[0]][d][v] + 45:
            distance[p[1]][p[0]][(d+1) % 4][0] = distance[p[1]][p[0]][d][v] + 45
            queue.put((distance[p[1]][p[0]][(d+1) % 4][0], p, (d+1) % 4, 0))
        if distance[p[1]][p[0]][(d-1) % 4][0] > distance[p[1]][p[0]][d][v] + 45:
            distance[p[1]][p[0]][(d-1) % 4][0] = distance[p[1]][p[0]][d][v] + 45
            queue.put((distance[p[1]][p[0]][(d-1) % 4][0], p, (d-1) % 4, 0))

        # moves
        if L[p[1]+moves[d][1]][p[0]+moves[d][0]] == "X":
            continue
        if v != 3:
            if distance[p[1]+moves[d][1]][p[0]+moves[d][0]][d][v+1] > distance[p[1]][p[0]][d][v] + velocity[v+1]:
                distance[p[1]+moves[d][1]][p[0]+moves[d][0]][d][v+1] = distance[p[1]][p[0]][d][v] + velocity[v+1]
                queue.put((distance[p[1]+moves[d][1]][p[0]+moves[d][0]][d][v+1], (p[0]+moves[d][0], p[1]+moves[d][1]), d, v+1))
        else:
            if distance[p[1]+moves[d][1]][p[0]+moves[d][0]][d][v] > distance[p[1]][p[0]][d][v] + velocity[v]:
                distance[p[1]+moves[d][1]][p[0]+moves[d][0]][d][v] = distance[p[1]][p[0]][d][v] + velocity[v]
                queue.put((distance[p[1]+moves[d][1]][p[0]+moves[d][0]][d][v], (p[0]+moves[d][0], p[1]+moves[d][1]), d, v))


A = (1, 1)
B = (8, 4)
L = ["XXXXXXXXXX",
     "X        X",
     "X XXXXXX X",
     "X XXXXXX X",
     "X        X",
     "XXXXXXXXXX"]
print(robot(L, A, B))
