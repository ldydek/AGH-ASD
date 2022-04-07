# f(i, j) - funkcja sprawdzająca, czy w tablicy A od A[0] do A[i] istnieje podciąg sumujący się do j
# f(i, j) = f(i-1, j) or f(i-1, j-A[i]) - albo dany element bierzemy do sumy, albo nie

def ex02(tab, t):
    n = len(tab)
    aux_tab = [[0 for _ in range(t+1)] for _ in range(n)]
    if tab[0] < t:
        aux_tab[0][tab[0]] = 1
    for x in range(n):
        aux_tab[x][0] = 1

    for x in range(1, n):
        for y in range(1, t+1):
            aux_tab[x][y] = aux_tab[x-1][y]
            if y >= tab[x]:
                aux_tab[x][y] = aux_tab[x-1][y] or aux_tab[x-1][y-tab[x]]
    return aux_tab[n-1][t]


tab = [3, 2, 4, 7, 8]
print(ex02(tab, 1))
