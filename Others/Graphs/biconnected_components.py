# [ENG] This algorithm solves problem of finding biconnected components in a graph. Biconnected component is
# a maximum set of edges for which each two edges of this set are part of a common simple circuit. First we find
# all bridges in a graph, then we remove them. The biconnected components are now simply the edges in the connected
# components, so for undirected graph for instance BFS will find all vertices and edges in one biconnected component.
# Time complexity: O(|V|+|E|)
# Space complexity: additional arrays: "parent", "visited", "low" and queue
# [PL] Podany algorytm rozwiązuje problem dwuspójnych składowych. Dwuspójną składową w grafie nazywamy maksymalny
# zbiór krawędzi, w którym każde dwie krawędzie leżą na wspólnym cyklu prostym. Na początku znajdujemy wszystkie
# mosty w grafie, by je usunąć. Teraz wszystkie spójne składowe są po prostu szukanymi dwuspójnymi składowymi.
# Aby je wyznaczyć możemy użyć chociażby BFS.
# Złożoność czasowa: O(|V|+|E|)
# Złożoność pamięciowa: dodatkowe tablice: "parent", "visited", "low" i kolejka
from queue import deque
from math import inf


def biconnected_components(graph):
    def dfs(graph, parent, x):
        nonlocal time
        time += 1
        visited[x] = time
        low[x] = time
        for y in range(n):
            if graph[x][y] != 0:
                if visited[y] == 0:
                    parent[y] = x
                    dfs(graph, parent, y)
                    low[x] = min(low[x], low[y])
                elif parent[x] != y:
                    low[x] = min(low[x], visited[y])

    n, time = len(graph), 0
    Q = deque()
    parent = [-1]*n
    visited = [0]*n
    low = [0]*n
    for x in range(n):
        if visited[x] == 0:
            dfs(graph, parent, x)
    for x in range(n):
        if parent[x] != -1 and low[x] == visited[x]:
            graph[parent[x]][x] = 0
            graph[x][parent[x]] = 0
    visited = [inf]*n
    ctr = 0
    for x in range(n):
        if visited[x] == inf:
            ctr += 1
            bfs(graph, Q, visited, x, ctr)
    return visited


def bfs(graph, Q, visited, s, ctr):
    n = len(graph)
    Q.append(s)
    while Q:
        u = Q.popleft()
        for x in range(n):
            if graph[u][x] == 1 and visited[x] == inf:
                visited[x] = ctr
                Q.append(x)


graph = [[0, 1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 0]]
print(biconnected_components(graph))
