# [ENG] Edmonds-Karp algorithm helps us solve a maximum flow problem in a flow network. We can imagine flow network
# as a directed graph in which weights of edges represent a capacity of this edge (canal). Idea is to constantly
# find path from source to sink and for that path compute maximum amount of material we can pass. It is of course
# minimum weight one of this path edge. After this, we modify graph to show that this edge we passed some substance,
# so for all edge capacities on this path we subtract from this capacity amount of passed substance. This operation
# also creates a back edge of weight equals to amount of passed substance, because later, we'll want to take this
# substance back if there will be another path from source to sink with bigger minimum capacity.
# Time complexity: O(|V||E|^2) - using BFS for finding paths from source to sink
# Space complexity: O(|V|) - additional arrays: parent, visited and queue for BFS
# [PL] Algorytm Edmondsa-Karpa pomaga nam rozwiązać problem maksymalnego przepływu w sieci przepływowej, którą możemy
# utożsamić ze skierowanym grafem, w którym wagi krawędzi informują o pojemności danego kanału w sieci. Pomysł polega
# na ciągłym znajdowaniu ścieżek powiększających od źródła do ujścia i dla takiej ścieżki obliczania ilości substancji,
# jaką można nią puścić jako minimum po wszystkich wagach krawędzi. Potem modyfikujemy naszą sieć, odejmując ilość
# puszczonej substancji od wszystkich krawędzi na znalezionej ścieżce powiększającej. Możliwe, że potem ilość tej
# substancji będziemy chceli wycofać i puścić innym kanałem, a więc w sieci residualnej tworzymy także krawędź
# o przeciwnym zwrocie i wadze równej ilości substancji, którą puściliśmy (tyle maksymalnie substancji będziemy mogli
# ewentualnie wycofać póżniej).
# Złożoność czasowa: O(|V||E|^2) - używając BFS do znajdowania ścieżek powiększających
# Złożoność pamięciowa: O(|V|) - dodatkowe tablice: parent, visited oraz kolejka dla BFS

from math import inf
from collections import deque


def bfs(graph, parent, s, t):
    n = len(graph)
    visited = [0]*n
    Q = deque()
    Q.append(s)
    visited[s] = 1
    while Q:
        u = Q.popleft()
        for x in range(n):
            if graph[u][x] != 0 and visited[x] == 0:
                visited[x] = 1
                parent[x] = u
                if x == t:
                    return True
                Q.append(x)


def edmonds_karp_algorithm(graph, s, t):
    n = len(graph)
    parent = [-1]*n
    max_flow = 0
    while bfs(graph, parent, s, t):
        flow = inf
        v = t
        while v != s:
            flow = min(flow, graph[parent[v]][v])
            v = parent[v]
        v = t
        max_flow += flow
        while v != s:
            graph[parent[v]][v] -= flow
            graph[v][parent[v]] += flow
            v = parent[v]
    return max_flow


graph = [[0, 9, 0, 0, 9, 0, 0], [0, 0, 7, 3, 0, 0, 0], [0, 0, 0, 4, 0, 0, 6], [0, 0, 0, 0, 0, 2, 9],
         [0, 0, 0, 3, 0, 6, 0], [0, 0, 0, 0, 0, 0, 8], [0, 0, 0, 0, 0, 0, 0]]
print(edmonds_karp_algorithm(graph, 0, 6))
