# [ENG] Program changing adjacency matrix to adjacency list and vice versa.
# [PL] Program zmieniający macierz sąsiedztwa na listę sąsiedztwa i odwrotnie.

def matrix_to_list(graph):
    n = len(graph)
    list = [[] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 1:
                list[x].append(y)
    return list


def list_to_matrix(list):
    n = len(list)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(len(list[x])):
            matrix[x][list[x][y]] = 1
    return matrix


matrix = [[0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
list = [[1, 2], [0], [0, 3, 5], [2, 4, 5], [3], [2, 3], []]
print(matrix_to_list(matrix))
print(list_to_matrix(list))
