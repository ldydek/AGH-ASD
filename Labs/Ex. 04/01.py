def ex01(A):
    n = len(tab)
    C = [0] * n
    B = [0] * n
    for x in range(n):
        A[x] = (A[x]//n, A[x] % n)
    counting_sort(A, B, C, 1)
    C = [0] * n
    counting_sort(A, B, C, 0)
    for x in range(n):
        B[x] = B[x][0]*n + B[x][1]
    return B


def counting_sort(A, B, C, index):
    n = len(A)
    for x in range(n):
        C[A[x][index]] += 1
    for x in range(1, n):
        C[x] += C[x-1]
    for x in range(n-1, -1, -1):
        B[C[A[x][index]]-1] = A[x]
        C[A[x][index]] -= 1
    for x in range(n):
        A[x] = B[x]
    return B


tab = [15, 32, 8, 63, 40, 11, 27, 53]
print(ex01(tab))
