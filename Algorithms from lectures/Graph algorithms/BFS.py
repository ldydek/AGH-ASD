# [ENG] In Breadth First Search (BFS) algorithm we research how graph looks like. We need here an additional data
# structure called a queue. At the beginning we add first chosen vertex and when algorithm works to the queue we will
# add only unvisited vertex (so part if the graph which is still not researched). Below is implementation of this idea
# for graph in adjacency matrix and list.
# Time complexity: O(V+E) for lists and O(V^2) for matrixes, where V is set of vertices and E number of edges between them
# Space complexity: O(V) - additional arrays of length V (visited, distance, parent)
# [PL] W algorytmie przeszukiwania wszerz (z ang. BFS) badamy jak graf wygląda. Będziemy tutaj potrzebowali dodatkowej
# struktury danych zwanej kolejką. Na początku do kolejki dodaję jeden wybrany wierzchołek i podczas działania algorytmu
# dla ściąganego wierzchołka z kolejki dodaję do niej wszystkich jego nieodwiedzonych sąsiadów.
# Złożoność obliczeniowa: O(V+E) dla list siąsiedztwa, O(V^2) - dla macierzy sąsiedztwa
# Złożonośc pamięciowa:  O(V) - dodatkowe tablice visited, distance oraz parent
from collections import deque
from math import inf


def bfs_m(graph, s):
    n = len(graph)
    distance = [inf]*n
    visited = [False]*n
    parent = [-1]*n
    visited[s], distance[s] = True, 0
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for x in range(n):
            if graph[u][x] == 1 and visited[x] is False:
                visited[x] = True
                distance[x] = distance[u] + 1
                parent[x] = u
                Q.append(x)
    return print_path(parent, 5)


def bfs_l(tab, s):
    n = len(tab)
    Q = deque()
    visited = [False]*n
    distance = [inf]*n
    parent = [-1]*n
    distance[s], visited[s] = 0, True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for x in range(len(tab[u])):
            if visited[tab[u][x]] is False:
                visited[tab[u][x]] = True
                distance[tab[u][x]] = distance[u] + 1
                parent[tab[u][x]] = u
                Q.append(tab[u][x])
    return print_path(parent, 5)


# [ENG] This function allows us to construct path from the initial vertex to any other if it exists.
# [PL] Ta funkcja pozwala nam odtworzyć dowolną ścieżkę w grafie między wierzchołkiem początkowym a jakimkolwiek innym
# (o ile ścieżka istnieje).
def print_path(parent, x):
    solution = []
    if parent[x] != -1:
        while parent[x] != -1:
            solution.append(x)
            x = parent[x]
        solution.append(x)
    return solution[::-1]


graph = [[0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
graph1 = [[1, 2], [0], [0, 3, 5], [2, 4, 5], [3], [2, 3], []]
print(bfs_m(graph, 0))
print(bfs_l(graph1, 0))
# [ENG] We start BFS from 0 vertex
# [PL] BFS zaczynamy od wierzchołka nr 0
