# Aby wyznaczyć dwuspójne składowe zadanego grafu, na początku uruhchamiam algorytm znajdujący mosty w grafie.
# Krawędzie, które są mostami, usuwam i uruchamiam BFS z wybranego wierzchołka dopóki nie odwiedzę wszystkich
# wierzchołków. Każdy zbiór wierzchołków odwiedzony za pomocą jednego wywołania BFS tworzy dwuspójną składową o ile
# zbiór nie składa się z jednego elementu (wierzchołka izolowanego). Inny sposób, to na takim grafie uruchomić algorytm
# wyznacznia spójnych składowych a warunek z wierzchołkami izolowanymi nadal trzeba uwzględnić.
from math import inf
from collections import deque


def biconnected_components(tab):
    def dfs_visit(x, visited, parent):
        nonlocal time
        nonlocal father
        nonlocal son
        time += 1
        visited[x] = time
        low[x] = time
        for y in range(len(tab[x])):
            if tab[x][y] == 1:
                if x == father and visited[y] == 0:
                    son += 1
                if parent[x] == y:
                    continue
                if visited[y] == 0:
                    parent[y] = x
                    dfs_visit(y, visited, parent)
                else:
                    low[x] = min(low[x], visited[y])
        if x != 0:
            low[parent[x]] = min(low[x], low[parent[x]])
    n = len(tab)
    visited = [0]*n
    parent = [-1]*n
    low = [inf]*n
    time = 0
    set1 = []

    for x in range(n):
        if visited[x] == 0:
            father = x
            son = 0
            dfs_visit(x, visited, parent)
    for x in range(n):
        if low[x] == visited[x] and x != 0:
            set1.append((parent[x], x))

    for x in range(len(set1)):
        graph[set1[x][0]][set1[x][1]] = 0
        graph[set1[x][1]][set1[x][0]] = 0

    for x in range(n):
        visited[x] = inf

    ctr = 1
    for x in range(n):
        if visited[x] == inf:
            bfs(graph, x, visited, ctr)
            ctr += 1
    return visited


def bfs(tab, s, visited, ctr):
    n = len(tab)
    ctr2 = 1
    visited[s] = ctr
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for x in range(n):
            if tab[u][x] == 1 and visited[x] == inf:
                visited[x] = ctr
                ctr2 += 1
                Q.append(x)
    if ctr2 == 1:
        visited[s] = inf


graph = [[0, 1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1, 0]]
print(biconnected_components(graph))
