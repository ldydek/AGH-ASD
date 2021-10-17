# [ENG] Floyd-Warshall algorithm solves problem of finding shortest paths in a graph between every pair of vertices.
# We allow for negative-weight edges but we assume there is no negative-weight cycles. This assumptions will help us
# compute real shortest paths. This is an example of a dynamic algorithm in a graph theory. For certain vertex "k"
# we want to check if computed path so far, for instance, between "i" and "j" is longer than sum of length of paths
# between "i" and "k" and "k" and "j". If so, we have to update our shortest path value. Algorithm works for graphs
# which are not consistent and for directed graphs as well.
# Time complexity: θ(|V|^3)
# Space complexity: θ(|V|^2) - two additional matrixes: for keeping values of computed paths and for constructing
# this paths
# [PL] Algorytm Floyda-Warshalla rozwiązuje problem znajdowania najkrótszych ścieżek pomiędzy dowolną parą wierzchołków.
# Zezwalamy na występowanie krawędzi z ujemnymi waga, lecz nie dopuszczamy pojawienia się ujemnego cyklu. Założenia
# te pozwolą obliczyć na prawdziwe najkrótsze ścieżki. Algorytm jest dynamiczny i polega na sprawdzeniu, czy dla danego
# pewnego wierzchołka "k" istnieje ścieżka z wierzchołka "u" do "v" krótsza od obecnej przechodząca przez "k".
# Algorytm działa także dla grafów niespójych w szczególności dla grafów skierowanych, w których nie można wskazać
# Złożoność obliczeniowa: θ(|V|^3)
# Złożoność pamięciowa: θ(|V|^2) - macierz przechowująca wyniki dla dowolnej pary wierzchołków w grafie
# oraz dodatkowo macierz poprzedników pozwalająca odtworzyć wybraną ściężkę powmiędzy dowolną parą wierzchołków,
# o ile oczywiście taka ścieżka istnieje.
from math import inf


def floyd_warshall_algorithm(tab):
    n = len(tab)
    distance = [[inf for _ in range(n)] for _ in range(n)]
    parent = [[-1 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        distance[x][x] = 0
    for x in range(n):
        for y in range(n):
            if tab[x][y] != 0:
                distance[x][y] = tab[x][y]
                parent[x][y] = x
    # [ENG] Basic cases: distance from "x" to "x" is 0 and initial values because of edges
    # [PL] Podstawowe warunki: odległość od "x" do "x" jest 0 oraz wartości krawędzi

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if distance[u][v] > distance[u][k] + distance[k][v]:
                    distance[u][v] = distance[u][k] + distance[k][v]
                    parent[u][v] = parent[k][v]
    return print_path(0, 5, parent)


def print_path(u, v, parent):
    path = []
    while u != v:
        path.append(v)
        v = parent[u][v]
    path.append(u)
    return path[::-1]


graph = [[0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 100, 0], [0, 0, 1, 0, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
print(floyd_warshall_algorithm(graph))
