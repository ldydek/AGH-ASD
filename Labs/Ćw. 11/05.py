# We split every vertex (let's call it "v") apart from source and sink to two vertices v' and v''. Later, we create 
# edges to v' if they were coming to "v", from v'' if they were coming from "v" and one edge (v',v''). All edges are
# directed. On this graph we can run Edmonds-Karp algorithm we will compute maximum flow and simultaneously the biggest
# number of vertex-separable paths.
# Time complexity: O(VE^2)
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
            if graph[u][x] != 0 and visited[x] == 0:
                visited[x] = 1
                parent[x] = u
                if x == t:
                    return True
                Q.append(x)


# Edmonds-Karp implementation
# we know after each BFS that maximum flow can be increased only by 1 (unitary edge weights)
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


# deleting edges coming to v'' and creating this ones that will be coming to v'
# directed edge (v',v'') is an exception
def modify_edges(graph, v, w):
    n = len(graph)
    for x in range(n):
        if graph[x][v] == 1 and x != w:
            graph[x][v] = 0
            graph[x][w] = 1


# splitting certain vertex to two vertices, so adjacency matrix has to be appropriately changed
def split_vertex(graph, v):
    n = len(graph)
    for x in range(n):
        graph[x].append(0)
    n += 1
    graph.append([0 for _ in range(n)])
    # creating edge (v', v'') here
    graph[n-1][v] = 1
    modify_edges(graph, v, n-1)


def ex05(graph, s, t):
    n = len(graph)
    for x in range(n):
        if x != s and x != t:
            split_vertex(graph, x)
    return edmonds_karp_algorithm(graph, s, t)


graph = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]
print(ex05(graph, 0, 9))
