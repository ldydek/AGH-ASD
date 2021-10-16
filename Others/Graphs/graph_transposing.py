# [ENG] Transpose graph means turn all edges directions. In matrix representation we can do in O(|V|^2) in place, but
# in list representation we are forced to allocate additional adjacency list but, on the other hand, we can do that
# operation in O(|V|+|E|), so possibly faster.
# [PL] Transponować graf to znaczy zmienić zwrot wszystkich krawędzi na przeciwny. W postaci macierzowej grafu możemy
# tego dokonać w miejscu w czasie O(|V|^2), natomiast w listowej reprezentacji musimy zaalokować sobie dodatkową listę
# sąsiedztwa, ale z drugiej strony tę operację jesteśmy w stanie wykonać w czasie O(|V|+|E|), a zatem możliwe że
# szybciej.

def graph_transpose_m(graph1):
    n = len(graph1)
    for x in range(n):
        for y in range(x+1, n):
            graph1[x][y], graph1[y][x] = graph1[y][x], graph1[x][y]
    return graph1


def graph_transpose_l(graph2):
    n = len(graph2)
    aux_tab = [[] for _ in range(n)]
    for x in range(n):
        for y in range(len(graph2[x])):
            aux_tab[graph2[x][y]].append(x)
    return aux_tab


graph1 = [[0, 1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0],
          [0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0]]
graph2 = [[1, 2], [5, 4], [3], [1, 6], [6], [6], []]
print(graph_transpose_m(graph1))
print(graph_transpose_l(graph2))
