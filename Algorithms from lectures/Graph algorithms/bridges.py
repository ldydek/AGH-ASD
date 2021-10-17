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

def bridges(graph):
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
#                   [ENG] "x" - vertex, "y" -its child
#                   [PL] "x" - wierzchołek, "y" - jego dziecko
                elif parent[x] != y:
                    low[x] = min(low[x], visited[y])
#                   [ENG] Back edge
#                   [PL] Krawędź wsteczna

    n, time = len(graph), 0
    parent = [-1]*n
    visited = [0]*n
    low = [0]*n
    solution = []
    for x in range(n):
        if visited[x] == 0:
            dfs(graph, parent, x)
    for x in range(n):
        if parent[x] != -1 and low[x] == visited[x]:
            solution.append((parent[x], x))
    return solution


graph = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1],
         [0, 0, 0, 1, 1, 0]]
print(bridges(graph))
