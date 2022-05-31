# Idea is to from given matrix create a directed acyclic graph (dag). In this graph edge (u,v) informs us that task "u"
# has to be done before task "v". At the end, we can sort given graph topologically and obtain correct sequence of
# vertices.
# Time complexity: O(n^2)
# Space complexity: O(n^2)
# Passed all tests

def dfs_visit(graph, visited, solution, s):
    for x in range(len(graph)):
        if graph[s][x] == 1 and visited[x] == 0:
            visited[x] = 1
            dfs_visit(graph, visited, solution, x)
    solution.append(s)


def dfs(graph):
    n = len(graph)
    visited = [0] * n
    solution = []
    for x in range(n):
        if visited[x] == 0:
            visited[x] = 1
            dfs_visit(graph, visited, solution, x)
    return solution[::-1]


def topological_sorting(graph):
    return dfs(graph)


def create_graph(T):
    n = len(T)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if T[x][y] == 1:
                graph[x][y] = 1
            elif T[x][y] == 2:
                graph[y][x] = 1
    return graph


def tasks(T):
    graph = create_graph(T)
    return topological_sorting(graph)


T = [[0, 0, 2, 1, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [2, 0, 0, 0, 0]]
print(tasks(T))
