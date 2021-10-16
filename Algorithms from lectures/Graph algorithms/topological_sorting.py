# Cały algorytm sortowania topologicznego polega na wywołaniu DFS-a z wybranego wierzchołka w grafie (źródła).
# W momencie kiedy jest on przetwarzany, dopisujemy go na początek nowo tworzonej listy, ponieważ mamy zagwarantowane,
# że żadna nowa krawędź z tego wierzchołka nie będzie wychodzić, która ewentualnie psułaby nasz porządek wierzchołków.
# Zmienną z wartością nonlocal można idealnie użyć w wypadku funkcji rekurencyjnych tak, aby wartość ta nie była
# modyfikowana przez powroty rekurencyjne np. zmienna "time" albo zbiór "set" w tym zadaniu.
# Warto także zauważyć, iż tablica processed to sortowania topologicznego nie jest w ogóle konieczna, ponieważ
# interesuje nas tylko fakt, że jeżeli wierzchołek został przetworzony to można go do zbioru dodać.
# Złożoność czasowa: O(V+E)
# Złożoność pamięciowa: O(V) - tablice visited i set, która zawiera posortowane wierzchołki
from math import inf


def topological_sorting(tab):
    n = len(tab)
    set = []
    visited = [0]*n

    def dfs_visit(tab, s):
        nonlocal set
        visited[s] = 1
        for x in range(len(tab[s])):
            if visited[tab[s][x]] == 0:
                dfs_visit(tab, tab[s][x])
        set.append(s)

    for x in range(n):
        if visited[x] == 0:
            dfs_visit(tab, x)
    return set[::-1]


tab = [[1, 2], [5, 4], [3], [6], [6], [6], []]
print(topological_sorting(tab))
