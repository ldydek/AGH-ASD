# If graph contains mother vertices (or vertex) one of them has to be this one which will be last processed during DFS
# traversal. At the end, we have to simply make second DFS traversal and check if all vertices are accessible from it.
# Time complexity: O(V+E)
# Space complexity: O(V)


def dfs(graph, visited, vertex, x):
    visited[x] = 1
    for u in graph[x]:
        if visited[u] == 0:
            dfs(graph, visited, vertex, u)
    vertex[0] = x


def ex02(graph):
    n = len(graph)
    visited = [0] * n
    vertex = [None]
    for x in range(n):
        if visited[x] == 0:
            dfs(graph, visited, vertex, x)
    visited = [0] * n
    dfs(graph, visited, vertex, vertex[0])
    for x in range(n):
        if visited[x] == 0:
            return False
    return True


graph = [[1],
         [2],
         [0, 3],
         [4],
         []]
print(ex02(graph))
