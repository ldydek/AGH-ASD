# Firstly, we sort given graph topologically and later all we have to do is to traverse array in which vertices are
# sorted in topological order. If between two adjacent elements in it there is no edge it means that in that dag there
# is not hamiltonian path.
# Time complexity: O(V+E)
# Space complexity: O(V)

def dfs_visit(graph, visited, x, solution):
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs_visit(graph, visited, i, solution)
    solution.append(x)


def dfs(graph):
    n = len(graph)
    solution = []
    visited = [0] * n
    for x in range(n):
        if visited[x] == 0:
            visited[x] = 1
            dfs_visit(graph, visited, x, solution)
    return solution[::-1]


def topological_sorting(graph):
    return dfs(graph)


def ex01(graph):
    n = len(graph)
    solution = topological_sorting(graph)
    for x in range(1, n):
        if solution[x] not in graph[solution[x-1]]:
            return False
    return True


graph = [[2], [], [1, 3], [4, 5], [], [4]]
print(ex01(graph))
