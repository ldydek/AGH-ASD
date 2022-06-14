# We use find-union technique to solve this task. Task is similar to Kruskal's algorithm, but this time we sort edge
# weights decreasingly and start adding it until A and B cities are not in one set. Thanks to it we will find a path
# between them in which minimum edge weight is possibly the highest (so tourists will be divided into lowest quantity
# of groups). Additionally, we can notice that given graph doesn't have to be consistent (only A and B have to be in
# one connected component).
# Time complexity: O(E log V)
# Space complexity: O(V)

from math import inf


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(x, y, parent, rank):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:
        rank[y] += 1
        parent[x] = y


def find_vertices_number(graph):
    v = 0
    for x in range(len(graph)):
        v = max(v, graph[x][0], graph[x][1])
    return v + 1


def ex05(graph, A, B, K):
    v = find_vertices_number(graph)
    graph.sort(key=lambda x: x[2], reverse=True)
    parent = [x for x in range(v)]
    rank = [0] * v
    value = inf
    for x, y, z in graph:
        if find(parent, x) != find(parent, y):
            union(x, y, parent, rank)
            value = min(value, z)
        if find(parent, A) == find(parent, B):
            if K/value == int(K/value):
                return K//value
            return K//value + 1


graph = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (7, 8, 7), (2, 8, 2), (6, 8, 6), (6, 7, 1), (5, 6, 2), (2, 3, 7),
         (2, 5, 4), (3, 5, 14), (3, 4, 9), (4, 5, 10)]
print(ex05(graph, 0, 4, 140))
