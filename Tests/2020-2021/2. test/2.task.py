# Idea is to run BFS algorithm from "s" and later from "t" vertex. Now suppose that "i" vertex is one of the vertices
# in the shortest path between "s" and "t". While considering all neighbours of "i" I check if distance from "s" to
# this neighbour plus distance from it to "t" is greater than shortest path distance. Thanks to BFS algorithms from "s"
# and "t" we have two shortest path trees rooted in "s" and "t", so after BFS it takes O(1) time to read distance
# between for instance "s" and any other vertex thanks to "distance" arrays.
# Time complexity: O(V+E) - two times BFS
# Space complexity: O(V)
# Passed all tests

from collections import deque
from math import inf


def bfs(G, distance, parent, s):
    queue = deque()
    queue.append(s)
    distance[s] = 0
    while queue:
        u = queue.popleft()
        for x in range(len(G[u])):
            if distance[G[u][x]] == inf:
                distance[G[u][x]] = distance[u] + 1
                parent[G[u][x]] = u
                queue.append(G[u][x])


# this function also takes O(V+E), because shortest path has at most |V| - 1 edges and for each vertex on this path we
# check its neighbours so it all sums up to O(E)
def follow_shortest_path(G, t, parent_s, distance_s, distance_t):
    length = distance_s[t]
    while parent_s[t] != -1:
        for x in range(len(G[t])):
            if length < distance_t[G[t][x]] + distance_s[G[t][x]]:
                return parent_s[t], t
        t = parent_s[t]
    return None


def enlarge(G, s, t):
    n = len(G)
    distance_s = [inf] * n
    distance_t = [inf] * n
    parent_s = [-1] * n
    parent_t = [-1] * n
    bfs(G, distance_s, parent_s, s)
    if distance_s[t] == inf:
        return None
    bfs(G, distance_t, parent_t, t)
    return follow_shortest_path(G, t, parent_s, distance_s, distance_t)


G = [[1, 2], [0, 2], [0, 1]]
s = 0
t = 2
print(enlarge(G, s, t))
