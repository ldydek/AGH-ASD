# Determining if cycle of length 4 exists in a graph given as adjacency matrix


# In this function I check whether certain two vertices have edges to the same two other vertices.
# If so, all four of them create a cycle of length 4.
def compare_rows(a, b):
    counter = 0
    for x in range(len(a)):
        if a[x] == 1 and b[x] == 1:
            counter += 1
        if counter == 2:
            return True
    return False


def ex03_O(graph):
    n = len(graph)
    for x in range(n):
        for y in range(x+1, n):
            if compare_rows(graph[x], graph[y]):
                return True
    return False


graph = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [0, 1, 1, 0, 1], [0, 1, 0, 1, 0]]
print(ex03_O(graph))
