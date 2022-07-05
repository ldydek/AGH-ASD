# Implementation of Prim's algorithm on adjacency matrix without using priority queue.
# Time complexity: O(V^2)
# Space complexity: O(V)

def prim_algorithm(graph, s):
    n = len(graph)
    distance = [float("inf") for _ in range(n)]
    distance[s] = float("-inf")
    parent = [-1] * n
    solution = []

    for x in range(n-1):
        for y in range(n):
            if graph[s][y] > 0 and distance[y] != float("-inf"):
                if distance[y] > graph[s][y]:
                    distance[y] = graph[s][y]
                    parent[y] = s
        index, value = None, float("inf")
        for y in range(n):
            if distance[y] != float("-inf") and distance[y] < value:
                value = distance[y]
                index = y
        distance[index] = float("-inf")
        solution.append((parent[index], index))
        s = index
    return solution


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
print(prim_algorithm(graph, 0))
