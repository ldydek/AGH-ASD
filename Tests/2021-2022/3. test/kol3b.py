# Lukasz Dydek
# Na wejściu właściwie dostajemy graf pełny, jeśli bierzemy pod uwagę loty szybowcami (wtedy też są krawędzie). A więc
# rozwiązanie sprowadza się do uruchomienia algorytmu Dijkstry. Trik polega tutaj na tym, iż nie używam kolejki
# priorytetowej a liniowo szukam następnego wierzchołka z minimalną wartością.
# Złożoność czasowa: O(n^2)
# Złożoność pamięciowa: O(n)

from kol3btesty import runtests


# O(n)
def choose_vertex(distance, visited):
    index, value = None, float("inf")
    for x in range(len(distance)):
        if distance[x] < value and visited[x] == 0:
            value = distance[x]
            index = x
    return index, value


# O(V+E)
def create_graph(G):
    n = len(G)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y, z in G[x]:
            graph[x][y] = z
            graph[y][x] = z
    return graph


# O(1)
def relax1(distance, graph, vertex, x):
    if distance[x] > distance[vertex] + graph[vertex][x]:
        distance[x] = distance[vertex] + graph[vertex][x]


# O(1)
def relax2(distance, vertex, x, A):
    if distance[x] > distance[vertex] + A[vertex] + A[x]:
        distance[x] = distance[vertex] + A[vertex] + A[x]


# O(n^2)
def airports(G, A, s, t):
    n = len(G)
    distance = [float("inf")] * n
    distance[s] = 0
    visited = [0] * n
    graph = create_graph(G)

    while True:
        vertex, value = choose_vertex(distance, visited)
        visited[vertex] = 1
        if vertex == t:
            return value
        for x in range(n):
            relax2(distance, vertex, x, A)
            if graph[vertex][x] > 0:
                relax1(distance, graph, vertex, x)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
