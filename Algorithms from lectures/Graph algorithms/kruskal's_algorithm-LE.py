# Algorytm Kruskala operuje na lesie zbiorów rozłącznych i oblicza MST w następujący sposób:
# 1) sortuje podaną listę krawędzi według najmniejszych wag
# 2) jeżeli rozważana w obecnej chwili krawędź ma dwa wierzchołki pochodzące z różnych zbiorów
# (a więc mające różnych reprezentantów), to zostaje ona dołączona do tworzonego MST.
# W przeciwieństwie do algorytmu Prima drzewa są tworzone niezależnie i te składające się z dużej liczby wierzchołków
# będą ze sobą łączone później za pomocą operacji Union.
# Złożoność czasowa: O(E lgV) - głównie dzięki funkcji odwrotnej do funkcji Ackermanna
# Złożoność pamięciowa: O(V) - tablice set, parent oraz rank

def kruskal_algorithm(tab):
    b = 0
    for x in range(len(tab)):
        b = max(b, tab[x][0], tab[x][1])
    v = b+1
    # ustalanie liczby wierzchołków z powodu podanej implementacji grafu jako listy krawędzi

    e = len(tab)
    set = []
    tab.sort(key=lambda x: x[2])
    # sortowanie według malejących wag

    parent = [x for x in range(v)]
    # v operacji MakeSet
    rank = [0]*v
    # tablica w celu łączenia drzew według rangi (mniejsze przepinamy do większego)

    for x in range(e):
        if find(parent, tab[x][0]) != find(parent, tab[x][1]):
            union(tab[x][0], tab[x][1], parent, rank)
            set.append((tab[x][0], tab[x][1]))
    # klasyczne operacje Find-Union na zbiorach rozłącznych
    return set


def find(parent, x):
    if x == parent[x]:
        return x
    x = find(parent, parent[x])
    return x


def union(x, y, parent, rank):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1


tab = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (7, 8, 7), (2, 8, 2), (6, 8, 6), (6, 7, 1), (5, 6, 2), (2, 3, 7),
       (2, 5, 4), (3, 5, 14), (3, 4, 9), (4, 5, 10)]
print(kruskal_algorithm(tab))
