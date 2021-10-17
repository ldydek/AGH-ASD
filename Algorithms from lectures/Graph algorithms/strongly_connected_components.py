# [ENG] Strongly connected component (scc) is a maximum set of vertices in a directed graph in which for each
# pair of vertices e.g. (u, v) there are paths from "u" to "v" and from "v" to "u". Here is the list of steps:
# 1) Do DFS and remember when vertex is being processed
# 2) Transpose graph
# 3) Do DFS one more time for decreasing processing time of vertices
# I'll try to explain it in just a few sentences. Transposing graph which has only one scc doesn't change anything,
# because two vertices will still be accessible between each other. If graph has more than one scc, it also has directed
# edges between one scc and another. So if we do DFS for transposed graph, edges between scc will change directions
# and this operation will prevent from going to different scc (through an edge which changed direction, so now it is
# impossible). All vertices visited by DFS create one scc. We repeat it until we visit every vertex.
# Time complexity: same as DFS
# Space complxity: O(V+E) for list representation for graph transposing and O(V) for matrix representation
# [PL] Silnie spójna składowa (z ang. scc) jest maksymalnym zbiorem wierzchołków w grafie skierowanym, w którym
# dowolne dwa wierzchołki są osiągalne nawzajem jeden z drugiego. Oto lista kroków:
# 1) Wywołaj algorytm DFS dla grafu, zapisując czasy przetworzenia wierzchołków
# 2) Transponuj graf
# 3) Wywołuj DFS dla wierzchołków po malejących czasach przetworzenia
# Powyżej po angielsku krótkie uzasadnienie, dlaczego ten algorytm działa poprawnie.
# Złożoność obliczeniowa: taka jak DFS
# Złożoność pamięciowa: O(|V|+|E|) dla reprezentacji listowej w celu transponowania grafu, O(V) dla macierzy sąsiedztwa

def scc(graph):
    n, logic, ctr = len(graph), False, 0
    visited = [0]*n
    stack = []
    solution = []
    for x in range(n):
        if visited[x] == 0:
            dfs(graph, x, visited, stack, logic, ctr, solution)
    transposed_graph = [[] for _ in range(n)]
    graph = graph_transposing(graph, transposed_graph)
    visited = [0]*n
    logic = True
    while stack:
        u = stack.pop()
        if visited[u] == 0:
            solution.append([])
            dfs(graph, u, visited, stack, logic, ctr, solution)
            ctr += 1
    return solution


def dfs(graph, x, visited, stack, logic, ctr, solution):
    visited[x] = 1
    if logic:
        solution[ctr].append(x)
    for y in range(len(graph[x])):
        if visited[graph[x][y]] == 0:
            dfs(graph, graph[x][y], visited, stack, logic, ctr, solution)
    if not logic:
        stack.append(x)


def graph_transposing(graph, tab_transpose):
    n = len(graph)
    for x in range(n):
        for y in range(len(graph[x])):
            tab_transpose[graph[x][y]].append(x)
    return tab_transpose


graph = [[1], [2], [3], [4], []]
print(scc(graph))
