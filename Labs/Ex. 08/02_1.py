# O(n^2)
# Musimy w O(n^2) sprawdzić, czy istnieje taki indeks w macierzy, dla którego w wierszy są same 0, a w kolumnie same 1
# z wyjątkiem A[i][i], gdzie będzie 0 (brak pętli).
# Wystarczy zaalokować dwie dodatkowe tablice każda długości "n". Jedna zawiera wyniki sumowania każdej kolumny, druga
# każdego wiersza. Teraz wystarczy sprawdzić, czy dla wiersza o sumie 0 odpawiadająca mu kolumna ma sumę n-1.

def ex02_1(graph):
    n = len(graph)
    sum_rows = [0] * n
    sum_column = [0] * n
    for x in range(n):
        for y in range(n):
            sum_rows[x] += graph[x][y]
            sum_column[x] += graph[y][x]
    for x in range(n):
        if sum_rows[x] == 0 and sum_column[x] == n-1:
            return x
    return None


graph = [[0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
print(ex02_1(graph))
