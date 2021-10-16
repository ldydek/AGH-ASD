# [ENG] Topological sorting means finding specific order of vertices for which, if we construct graph, edges will be
# only from left to right, so we can perform it only in dags (directed acyclic graphs). Whole algorithm goes on using
# DFS. If certain vertex is being processed we are adding it at the end of new created list. At the end, we reverse
# that list. This algorithm works, because when certain vertex is processed we have a certainty that any other edge
# doesn't start from that vertex (that could go to other vertex, which is not processed).
# Time complexity: same as DFS
# Space complexity: O(V) - "visited" array for marking already visited vertices ("processed" array is not necessary)
# and array for solution
# [PL] Sortowanie topologiczne polega na znalezieniu takiej kolejności wierzchołków w grafie, dla której jeśli
# skonstruowalibyśmy graf, to krawędzie łączyłyby wierzchołki od lewej do prawej, a zatem możemy tego dokonać
# tylko w dagach (skierowanych grafach acyklicznych). Cały algorytm sortowania topologicznego polega na wywołaniu
# DFS-a z wybranego wierzchołka w grafie (źródła). W momencie kiedy jest on przetwarzany, dopisujemy go
# na początek nowo tworzonej listy, ponieważ mamy zagwarantowane, że żadna nowa krawędź z tego wierzchołka
# nie będzie wychodzić, która ewentualnie psułaby nasz porządek wierzchołków i prowadziła do 
# wierzchołka, który jeszcze przetworzony nie był. Warto także zauważyć, iż tablica "processed" do sortowania
# topologicznego nie jest w ogóle konieczna, ponieważ interesuje nas tylko fakt, że jeżeli wierzchołek został
# przetworzony to można go do zbioru dodać.
# Złożoność czasowa: taka sama jak DFS
# Złożoność pamięciowa: O(V) - tablice "visited" dla zaznaczania już odwiedzonych wierzchołków oraz tablica dla
# rozwiązania.
def topological_sorting(graph):
    n = len(graph)
    set = []
    visited = [0]*n
    for x in range(n):
        if visited[x] == 0:
            dfs_visit(graph, set, visited, x)
    return set[::-1]


def dfs_visit(graph, set, visited, s):
    visited[s] = 1
    for x in range(len(graph[s])):
        if visited[graph[s][x]] == 0:
            dfs_visit(graph, set, visited, graph[s][x])
    set.append(s)


graph = [[1, 2], [5, 4], [3], [1, 6], [6], [6], []]
print(topological_sorting(graph))
