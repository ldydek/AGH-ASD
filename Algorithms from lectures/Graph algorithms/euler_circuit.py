# Dla grafu nieskierowanego cykl Eulera można znaleźć w następujący sposób:
# 1) sprawdzamy warunki konieczne, a więc spójność jednym wywołaniem BFS (prostszym w implementacji imo)
# oraz czy stopień każdego wierzchołka jest parzysty
# 2) Jeżeli warunki konieczne są spełnione, to wywołujemy algorytm DFS z dowolnego wierzchołka i w momencie
# przetworzenia dodajemy go na początek listy wierzchołków tworzących cykl Eulera.
# To co jest nietypowe w tym algorytmie to fakt, iż jako odwiedzone oznaczamy krawędzie a nie wierzchołki.


# implementation without checking graph consistency 
# checking whether graph is Eulerian
# (even degree vertices)
def checking(graph):
    n = len(graph)
    degree = [0] * n
    for x in range(n):
        for y in graph[x]:
            degree[y] += 1
    for x in range(n):
        if degree[x] % 2 == 1:
            return False
    return True


def dfs(graph, visited, solution, x):
    for v in graph[x]:
        if visited[x][v] == 0:
            visited[x][v] = 1
            visited[v][x] = 1
            dfs(graph, visited, solution, v)
    solution.append(x)


def euler_cycle(graph):
    n = len(graph)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    solution = []
    if checking(graph) is False:
        return False
    dfs(graph, visited, solution, 0)
    return solution


graph = [[1, 3, 4, 5], [0, 2], [1, 3], [0, 2], [0, 5], [0, 4]]
print(euler_cycle(graph))
