# Rozważając dane pole macierzy A[i][j], mamy dwa przypadki. Jeśli A[i][j] = 0, to "j" nie może być ujściem, więc
# wierzchołek "j" odrzucamy i przechodzimy do "j+1". Natomiast jeśli A[i][j] = 1, to znowu "i" nie może być ujściem,
# więc "i" odrzucamy i przechodzimy do "i+1". Gdy mamy A[i][i], to idziemy do "i+1", nie odrzucając "i", ponieważ
# komórka w macierzy (i, i) zawsze będzie zerem (nie dopuszczamy pętli). Na koniec sprawdzamy, czy indeks, który został,
# faktycznie jest uniwersalnym ujściem.


# O(n)
def ex02_2(graph):
    n = len(graph)
    ctr = 0
    a, b = 0, 0
    index = None
    while b < n:
        if graph[a][b] == 1:
            a += 1
            ctr += 1
            index = b
        else:
            if a != b:
                ctr += 1
            b += 1
            index = a
    suma = 0
    for x in range(n):
        suma += graph[x][index]
    if sum(graph[index]) == 0 and suma == n-1:
        return index
    return None


graph = [[0, 0, 0, 0, 0, 1],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]
print(ex02_2(graph))
