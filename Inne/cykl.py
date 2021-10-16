# Za pomocą DFS i lasu przeszukiwania wgłąb obliczam taki cykl w podanym grafie, który posiada najmniejszą ilość
# krawędzi. Algorytm operuje na krawędziach wstecznych oraz różnicy w czsach odwiedzenia wierzchołków, pomiędzy
# którymi taka krawędź wsteczna istnieje w lesie przeszukiwania wgłąb.


from math import inf


def dfs(graph):
    def dfs_visit(graph, s):
        nonlocal time
        nonlocal solution
        time += 1
        visited[s] = time
        for x in range(len(graph[s])):
            if visited[graph[s][x]] == 0:
                parent[graph[s][x]] = s
                dfs_visit(graph, graph[s][x])
            if visited[graph[s][x]] < visited[s] and parent[graph[s][x]] != s and parent[s] != graph[s][x]:
                solution = min(solution, (visited[s] - visited[graph[s][x]], s, graph[s][x]))
    n = len(graph)
    visited = [0]*n
    parent = [-1]*n
    time = 0
    solution = (inf, inf, inf)
    for x in range(n):
        if visited[x] == 0:
            dfs_visit(graph, x)
    return print_path(parent, solution[1], solution[2])


def print_path(parent, a, b):
    set = [a]
    while parent[a] != b:
        a = parent[a]
        set.append(a)
    set.append(b)
    return set[::-1]


graph = [[6, 7], [4, 5, 6], [3, 6], [2, 4], [1, 3], [1, 7], [0, 1, 2], [0, 5]]
print(dfs(graph))
