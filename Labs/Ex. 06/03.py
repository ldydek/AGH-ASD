# f(i, j) - funkcja określająca, czy samochody od A[0] do A[i] mogą wjechać na dwa pasy tak, aby na górnym pozostało
# "j" miejsca wolnego
# Rekurencja: f(i, j) = f(i-1, j+A[i]) or f(i-1, j), jeśli j+A[i] <= L (auta mieszczą się na górnym pokładnie) oraz
# sum(A[x])+y <= 2L (warunek na miejsce dla auta na drugim pasie), ponieważ:
# L-j - miejsce jakie zajmują auta na pierwszym pasie,
# sum(A[x-1]-(L-y) - miejsce jakie zajmują auta na drugim pasie,
# więc sprawdzamy, czy możemy na ten drugi pas dodać kolejne auto - sum(A[x]) - L + y <= L
# więc ostatecznie sum(A[x]) + y <= 2L


def find_index(aux_tab):
    n = len(aux_tab)
    for x in range(n - 1, -1, -1):
        for y in range(L + 1):
            if aux_tab[x][y] == 1:
                return x, y


def ex03(A, L):
    n = len(A)
    for x in range(1, n):
        A[x] += A[x-1]
    aux_tab = [[0 for _ in range(L+1)] for _ in range(n)]
    solution = [-1] * n
    if L < A[0]:
        return False
    aux_tab[0][L-A[0]] = 1
    aux_tab[0][L] = 1
    for x in range(1, n):
        for y in range(L+1):
            if y + A[x] - A[x-1] <= L:
                aux_tab[x][y] = aux_tab[x-1][y+A[x]-A[x-1]]
            if A[x] + y <= 2*L:
                aux_tab[x][y] = aux_tab[x][y] or aux_tab[x-1][y]
    indexes = find_index(aux_tab)
    print_solution(aux_tab, indexes, solution, A)
    return solution


def print_solution(aux_tab, indexes, solution, A):
    n = len(aux_tab)
    k = indexes[0]
    for x in range(k, 0, -1):
        if aux_tab[indexes[0]][indexes[1]] == aux_tab[indexes[0]-1][indexes[1]]:
            solution[x] = 0
            indexes = (indexes[0]-1, indexes[1])
        else:
            solution[x] = 1
            indexes = (indexes[0]-1, indexes[1]+A[x]-A[x-1])
    sum = 0
    for x in range(1, n):
        if solution[x] == 1:
            sum += A[x]
    if A[0] + sum <= L:
        solution[0] = 1
    else:
        solution[0] = 0


A = [8, 3, 3, 1, 1]
L = 8
print(ex03(A, L))
