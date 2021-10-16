# Elementarny algorytm przeszukiwania wszerz grafu (BFS)
# Dla ściąganego wierzchołka z kolejki dodaje do niej wszystkich jego NIEODWIEDZONYCH sąsiadów, a algorytm się
# kończy wówczas, gdy kolejka jest pusta i "fala" rozeszła się po wszystkich możliwych wierzchołkach.
# Gdy graf jest niespójny  komórki w tablicy distance dla odpowiednich wierzchołków pozostaną z wartością inf.
# Złożoność obliczeniowa: O(V^2) - reprezentacja macierzowa
# Złożonośc pamięciowa:  O(V) - dodatkowe tablice visited, distance oraz parent
# W celu wywołania BFS na niespójnym grafie iterować po tablicy visited do pierwszego elementu z wartością False?
from collections import deque
from math import inf


def bfs(tab, s):
    n = len(tab)
    distance = [inf]*n
    visited = [False]*n
    parent = [inf]*n
    parent[s] = -1
    visited[s] = True
    distance[s] = 0
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for x in range(n):
            if tab[u][x] == 1 and visited[x] is False:
                visited[x] = True
                distance[x] = distance[u] + 1
                parent[x] = u
                Q.append(x)
    return parent


def print_solution(parent, x):
    if parent[x] == inf:
        return False
    else:
        if parent[x] != -1:
            print_solution(parent, parent[x])
        print(x, end=" ")


tab = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0]]
print(bfs(tab, 0))
tab1 = bfs(tab, 0)
print(print_solution(tab1, 4))
