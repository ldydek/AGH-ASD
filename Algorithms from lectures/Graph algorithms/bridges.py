# [ENG] Bridge in undirected graph is an edge whose deletion will cause disconnection of the graph. Here is list of
# steps how we can find all bridges:
# 1) Run DFS from any vertex and write down visited time of each vertex
# 2) For each vertex compute low(v), where "v" is a certain vertex in a graph
# low(v) = min(d(v), min(d(u)), min(low(w))), where "u" is a vertex for which there is a back edge from "v" to "u"
# in a DFS tree and "w" is a child of "v" in a DFS tree
# Bridge is an edge (v, p(v)) for which d(v) = low(v), where p(v) means parent of "v" in a DFS tree.
# Why does it work? Bridge can't be a part of a simple circuit in a graph, because deletion won't cause disconnection.
# This formula for "low" function helps us detect a cycle and shows from which vertex this cycle starts.
# That's why if this vertex is for example "v" it and its parent (if it exists) create a bridge.
# Time complexity: O(|V|+|E|) - same as DFS
# Space complexity: O(|V|) - additional arrays: low, visited, parent and for keeping already found bridges
# (each edge can be a bridge)
# [PL] Mostem w grafie nieskierowanym nazywamy krawędź, której usunięcie zwiększy ilość spójnych składowych grafu.
# Poniżej lista kroków jak wyznaczyć wszystkie mosty:
# 1) Wykonaj DFS dla dowolnego wierzchołka startowego i zapisuj czasu odwiedzenia
# 2) Dla każdego wierzchołka policz wartość low(v) daną wzorem: low(v) = min(d(v), min(d(u)), min(low(w))), gdzie
# "u" jest wierzchołkiem, dla którego istnieje w drzewie DFS krawędź wsteczna (v, u), a "w" jest dzieckiem "v" w drzewie
# DFS (o ile "v" ma potomków). Nieformalne i krótkie rozumowanie, dlaczego to działa zostało przedstawione w języku
# angielskim powyżej.
# Złożoność czasowa: O(|V|+|E|) - taka jak w DFS
# Złożoność pamięciowa: O(|V|) - dodatkowej tablice: low, visited, parent i dla trzymania rozwiązania

from math import inf


def dfs(graph, distance, low, parent, time, x):
    time[0] += 1
    distance[x] = time[0]
    low[x] = time[0]
    for v in graph[x]:
        if distance[v] == inf:
            parent[v] = x
            low[x] = min(low[x], dfs(graph, distance, low, parent, time, v))
        elif parent[x] != v:
            low[x] = min(low[x], distance[v])
    return low[x]


def bridges(graph):
    n = len(graph)
    distance = [inf] * n
    low = [inf] * n
    parent = [-1] * n
    time = [0]
    for x in range(n):
        if distance[x] == inf:
            dfs(graph, distance, low, parent, time, x)
    solution = []
    for x in range(n):
        if distance[x] == low[x] and parent[x] != -1:
            solution.append((parent[x], x))
    return solution


graph = [[1, 4], [0, 2], [1, 3, 4], [2], [0, 2, 5], [4, 6, 7], [5, 7], [5, 6]]
print(bridges(graph))
