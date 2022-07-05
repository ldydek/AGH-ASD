# Idea is to from given matrix create a directed acyclic graph (dag). In this graph edge (u,v) informs us that task "u"
# has to be done before task "v". At the end, we can sort given graph topologically and obtain correct sequence of
# vertices. Note that allocating another matrix for a graph is not necessary, because when given matrix as an input
# has 1 value edge is in correct direction. We have to only change edge direction, when a certain matrix field has 2.
# Time complexity: O(n^2)
# Space complexity: O(n) - recursion
# Passed all tests

def topological_sorting(graph, visited, v, order):
    n = len(graph)
    for x in range(n):
        if graph[v][x] == 1 and visited[x] == 0:
            visited[x] = 1
            topological_sorting(graph, visited, x, order)
    order.append(v)

    
def tasks(T):
    n = len(T)
    for x in range(n):
        for y in range(n):
            if T[x][y] == 2:
                T[x][y] = 0
                T[y][x] = 1
    order = []
    visited = [0] * n
    for x in range(n):
        if visited[x] == 0:
            visited[x] = 1
            topological_sorting(T, visited, x, order)
    return order[::-1]


T = [[0, 0, 2, 1, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [2, 0, 0, 0, 0]]
print(tasks(T))
