# We can create transitive closure of a given graph using Floyd-Warshall algorithm. If we suppose that adjacency matrix
# has only 0-1 values we can get a transitive closure without need to allocate second matrix. Using dynamic programming
# and logical operators we can create an edge from, for instance, (u,v) if for certain "k" there were edges (u,k) and
# (k,v) (paths from "u" to "k" and from "k" to "v" in an input graph).
# Time complexity: O(V^3)
# Space complexity: O(1)


def transitive_closure(graph):
    n = len(graph)
    for k in range(n):
        for x in range(n):
            for y in range(n):
                if x == y:
                    continue
                graph[x][y] = graph[x][y] or (graph[x][k] and graph[k][y])
    return graph


graph = [[0, 1, 0, 1, 0, 0],
         [1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 1, 0]]
print(transitive_closure(graph))
