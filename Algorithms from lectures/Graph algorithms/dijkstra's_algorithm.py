# [ENG] Dijkstra's algorithm solves problem of finding shortest paths from certain vertex (source) to any other
# vertex in a given graph in which edges have nonnegative weights. Idea is to use additional data structure - priority
# queue, which helps us find a vertex with shortest path from source (from vertices still in priority queue). When we
# find suitable candidate we can perform number of relaxation of edges which go from that vertex. It means we check
# whether path to "v" through "u" is shorter than shortest path found so far (considering edge (u, v)).
# To priority queue we add tuples (distance from source, vertex). Result of this algorithm is a shortest paths tree.
# Note that if graph is in matrix representation there is no need to allocate priority queue, because during traversing
# row in a matrix and looking for an edge I can also iterate in my "distance" array and find vertex in a graph, which
# doesn't have computed real distance from the source.
# Time complexity: O(E lg V)
# Space complexity: O(V)
# [PL] Algorytm Dijkstry rozwiązuje problem znajdowania najkrótszych ścieżek ze źródła do każdego innego wierzchołka
# w grafie o nieujemnych wagach. Używamy w nim dodatkowej struktury danych - kolejki priorytetowej, która pomaga nam
# znaleźć wierzchołek grafu, dla którego długość ścieżki od źródła do niego jest najmniejsza (spośród wierzchołków
# nadal w kolejce). Kiedy znajdziemy odpowiedniego kandydata wykonujemy szereg relaksacji krawędzi wychodzących
# z tego wierzchołka. Relaksacja krawędzi (u, v) polega na sprawdzeniu, czy idąc do wierzchołka "v" przez "u" nie
# zmniejszymy odległości dotychczas znalezionej. Do kolejki dodajemy krotki postaci
# (odległość od źródła, nr wierzchołka). Wynikiem działania algorytmu jest drzewo najkrótszych ścieżek.
# Warto zauważyć, że w przypadku reprezentacji macierzowej grafu nie jest konieczne alokowanie kolejki, ponieważ
# podczs liniowego przechodzenia przez rząd macierzy w poszukiwaniu krawędzi tę samą operację mogę zrobić w tablicy
# "distance", szukając wierzchołka, dla którego nie została jeszcze wyznaczona długość najkrótszej ścieżki.
# Złożoność obliczeniowa: O((V+E)lgV) = O(ElgV) dla kolejki priorytetowej jako kopca binarnego
# Złożoność pamięciowa: O(V) - kolejka priorytetowa (kopiec binarny) ze wszytkimi wierzchołkami.
from math import inf
from queue import PriorityQueue


def dijkstras_algorithm_l(graph1, s):
    n = len(graph1)
    distance = [inf]*n
    distance[s] = 0
    visited = [False]*n
    Q = PriorityQueue()
    Q.put((0, s))
    parent = [-1]*n

    while not Q.empty():
        u = Q.get()
        v = u[1]
        if visited[v] is False:
            visited[v] = True
            for x in range(len(graph1[v])):
                if visited[graph1[v][x][0]] is False:
                    # [ENG] relaxation
                    # [PL] relaksacja
                    if distance[graph1[v][x][0]] > distance[v] + graph1[v][x][1]:
                        distance[graph1[v][x][0]] = distance[v] + graph1[v][x][1]
                        parent[graph1[v][x][0]] = v
                        Q.put((distance[graph1[v][x][0]], graph1[v][x][0]))
    return print_path(parent, 4)


def dijkstras_algorithm_m(graph2, s):
    n = len(graph2)
    distance = [inf]*n
    distance[s] = 0
    visited = [False]*n
    parent = [-1]*n

    while True:
        v1, v2 = inf, inf
        for x in range(n):
            if visited[x] is False and distance[x] < v1:
                v1 = distance[x]
                v2 = x
        if v1 == inf:
            break
        visited[v2] = True
        for x in range(n):
            if graph2[v2][x] != 0 and visited[x] is False:
                # [ENG] relaxation
                # [PL] relaksacja
                if distance[x] > distance[v2] + graph2[v2][x]:
                    distance[x] = distance[v2] + graph2[v2][x]
                    parent[x] = v2
    return print_path(parent, 4)


def print_path(parent, x):
    solution = []
    if parent[x] == -1:
        return solution
    while parent[x] != -1:
        solution.append(x)
        x = parent[x]
    solution.append(x)
    return solution[::-1]


graph1 = [[(1, 4), (7, 8)], [(0, 4), (2, 8), (7, 11)], [(1, 8), (3, 7), (5, 4), (8, 2)], [(2, 7), (4, 9), (5, 14)],
       [(3, 9), (5, 10)], [(2, 4), (3, 14), (4, 10), (6, 2)], [(5, 2), (7, 1), (8, 6)], [(0, 8), (1, 11), (6, 1), (8, 7)],
       [(2, 2), (6, 6), (7, 7)]]
graph2 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
print(dijkstras_algorithm_l(graph1, 0))
print(dijkstras_algorithm_m(graph2, 0))
