# Idea is to change all graph weight to its logarithm with, for instance, base 2 (it doesn't really matter) and change
# sign number to opposite. Now we can run Bellman-Ford algorithm on that graph and check whether negative cycle exists.
# and if it is accessible from the source. We can omit second condition, because given graph is complete.
# Time complexity: O(V^3)
# Space complexity: O(V)

from math import log
from math import inf


def exchange(K):
    n = len(K)
    for x in range(n):
        for y in range(x+1, n):
            K[y][x] = 1/K[x][y]
    # if we need 2 pieces of "x" to obtain "y" it means that we need 1/2 pieces of "y" to obtain "x"
    for x in range(n):
        for y in range(n):
            if K[x][y] > 0:
                K[x][y] = -log(K[x][y], 2)
    # now on the given matrix we can simply run Bellman-Ford algorithm
    return bellman_ford_algorithm(K, 0)


# edge relaxation
def relax(y, z, distance, parent, tab):
    if distance[z] > distance[y] + tab[y][z] and parent[y] != z:
        distance[z] = distance[y] + tab[y][z]
        parent[z] = y


# basic Bellman-Ford algorithm implementation
def bellman_ford_algorithm(tab, s):
    n = len(tab)
    distance = [inf]*n
    distance[s] = 0
    parent = [-1]*n

    for x in range(n-1):
        for y in range(n):
            for z in range(n):
                if tab[y][z] != 0:
                    relax(y, z, distance, parent, tab)

    for y in range(n):
        for z in range(n):
            if tab[y][z] != 0:
                if distance[z] > distance[y] + tab[y][z] and parent[y] != z:
                    return True
    return False


K = [[0, 2, 4, 5, 3],
     [0, 0, 1, 3, 2],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 0, 2],
     [0, 0, 0, 0, 0]]
print(exchange(K))
