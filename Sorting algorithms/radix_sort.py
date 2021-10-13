# Algorytm sortowania pozycyjnego. Opiera się wywoływaniu kilkukrotnie algorytmu sortowania przez zliczanie, zaczynając
# od najmniej znaczących cyfr. Kluczowy w poprawnym działaniu tego algorytmu jest fakt, iż sortowanie przez zliczanie
# jest algorytmem stabilnym.
# Złożoność czasowa: O(d(n+k)) = O(n+k), gdzie d jest ilością cyfr w liczbach


def count_sort(A, k):
    a = A[0]
    ctr = 0
    while a > 0:
        ctr += 1
        a //= 10

    for b in range(ctr):
        C = [0]*k
        B = [0]*len(A)
        for x in range(len(A)):
            index = (A[x]//10**b) % 10
            C[index] += 1
        for x in range(1, k):
            C[x] += C[x-1]
        for x in range(len(A)-1, -1, -1):
            B[C[(A[x]//10**b) % 10]-1] = A[x]
            C[(A[x]//10**b) % 10] -= 1
        for x in range(len(A)):
            A[x] = B[x]
    return A


tab = [329, 457, 657, 839, 436, 720, 355]
n = len(tab)
print(tab)
print(count_sort(tab, 10))
