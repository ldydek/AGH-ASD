# [ENG] In Depth First Search (DFS) algorithm we research how graph looks like. In this case, we don't need any
# extra data structures like queues (simply additional array is efficient). We start from certain vertex (source) and
# for each unvisited neighbour of this vertex we recursively call a function to move further in a graph. During
# recursive returns vertex is also processed and this data we also have to keep in aadditional array. Result of this
# algorithm is DFS forest. Below is presented implementation of this idea for adjacency matrixes and lists.
# Time complexity: O(V+E) for adjacency lists and O(V^2) for adjacency matrixes
# Space complexity: O(V) - additional arrays (visited, processed, parent)
# [PL] Elementarny algorytm grafowy przeszukiwania w głąb. Dzięki niemu może zbadać wygląd grafu. Zaczynamy z wybranego
# przez nas wierzchołka (źródła) i dla wszystkich nieodwiedzonych wierzchołków grafu rekurencyjnie wywołujemy funkcję
# celem przemieszczenia się w grafie dalej. Podczas rekurencyjnych powrotów dany wierzchołek jest przetwarzany i dane
# te są również pamiętane w dodatkowej tablicy. Wynikiem działania algorytmu jest las przeszukiwania w głąb. Poniżej
# została zaimplementowana idea DFS dla macierzy sąsiedztwa i list sąsiedztwa.
# Złożoność obliczeniowa: O(V^2) dla reprezentacji macierzowej grafu i O(V+E) dla listowej
# Złożoność pammięciowa: O(V) - dodatkowe tablice (visited, processed oraz parent)

def dfs_m(graph):
    def dfs_visit(graph, x, visited, parent, processed):
        nonlocal time
        time += 1
        visited[x] = time
        for y in range(n):
            if graph[x][y] == 1 and visited[y] == 0:
                parent[y] = x
                dfs_visit(graph, y, visited, parent, processed)
        time += 1
        processed[x] = time

    time, n = 0, len(graph)
    visited = [0]*n
    processed = [0]*n
    parent = [-1]*n
    for x in range(n):
        if visited[x] == 0:
            dfs_visit(graph, x, visited, parent, processed)
    return print_path(parent, 5)


def print_path(parent, x):
    solution = []
    if parent[x] == -1:
        return solution
    while parent[x] != -1:
        solution.append(x)
        x = parent[x]
    solution.append(x)
    return solution[::-1]


graph = [[0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
print(dfs_m(graph))
