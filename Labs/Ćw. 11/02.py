# Each graph edge has an unitary weight. According to max-flow min-cut theorem after picking random "s" (source) and
# "t" (sink) we will get maximum flow and simultaneously minimum number of edge we have to remove to obtain two
# components and "s" will be in different one that "t". We know that it has to be a vertex that will be in different
# component than "s", so we can consider |V|-1 flow networks and choose minimum from all minimum cuts. That will be
# a solution. Additionally, we can point edges that should be removed, because they don't exist in residual graph (only
# back edges with beginning capacity).
# Time complexity: O(V^2 * E^2)
# Space complexity: O(V^2)

from collections import deque


def bfs(graph, parent, s, t):
    n = len(graph)
    visited = [0] * n
    Q = deque()
    Q.append(s)
    visited[s] = 1
    while Q:
        u = Q.popleft()
        for x in range(n):
            if graph[u][x] == 1 and visited[x] == 0:
                visited[x] = 1
                parent[x] = u
                if x == t:
                    return True
                Q.append(x)


# Edmonds-Karp algorithm implementation
# one difference from the basic version is that we don't have to follow expanding path, because we know that
# after each BFS flow will be 1 (unitary weights)
def edmonds_karp_algorithm(graph, s, t):
    n = len(graph)
    parent = [-1] * n
    max_flow = 0
    while bfs(graph, parent, s, t):
        max_flow += 1
        v = t
        while v != s:
            graph[parent[v]][v] -= 1
            graph[v][parent[v]] += 1
            v = parent[v]
    return max_flow


# function return graph copy
# it is obligatory, because after each maximum flow algorithm we destroy input graph and get residual graph
def graph_copy(graph):
    n = len(graph)
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            new_graph[x][y] = graph[x][y]
    return new_graph


# vertex 0 is our constant source and we compute min-cut for sinks from 1 to |V|-1
def ex02(graph):
    n = len(graph)
    solution = 10**10
    for x in range(1, n):
        new_graph = graph_copy(graph)
        solution = min(solution, edmonds_karp_algorithm(new_graph, 0, x))
    return solution


graph = [[0, 1, 0, 0, 1, 1],
         [1, 0, 1, 1, 0, 0],
         [0, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [1, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 1, 0]]
print(ex02(graph))
