# f(i, j) - długość najdłuższego wspólnego podciągu, uwzględniając "i" pierwszych elementów pierwszej tablicy oraz
# "j" pierwszych elementów drugiej
# A, B - dane tablice z danymi
# f(i, j) = {f(i-1, j-1) + 1 jeśli A[i] = B[j], max(f(i-1, j), f(i, j-1) wpp}
# Warunki brzegowe:
# f(0, j) = {1 jeśli A[0] = B[j], 0 wpp}
# f(i, 0) = {1 jeśli A[i] = B[0], 0 wpp}
# Rozwiązanie: f(n-1, m-1), gdzie n = A.length oraz m = B.length


def ex03(A, B):
    n = len(A)
    m = len(B)
    aux_tab = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(m):
        if A[0] == B[x]:
            aux_tab[0][x] = 1
    for x in range(n):
        if A[x] == B[0]:
            aux_tab[x][0] = 1
    for x in range(1, n):
        for y in range(1, m):
            if A[x] == B[y]:
                aux_tab[x][y] = aux_tab[x-1][y-1] + 1
            else:
                aux_tab[x][y] = max(aux_tab[x-1][y], aux_tab[x][y-1])
    return aux_tab[n-1][m-1]


X = "AGGTAB"
Y = "GXTXAYB"
print(ex03(X, Y))
