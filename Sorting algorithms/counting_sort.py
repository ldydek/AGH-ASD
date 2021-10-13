# Sortowanie przez zliczanie
# Złożoność obliczeniowa: O(n+k), gdzie k jest rozmiarem dodatkowo zaalokowanej tablicy
# n - zakres danych
# Uwaga! Dane muszą być liczbami całkowitymi i pochodzić z małego zakresu.
# Liczby ujemne też mogą wystąpić i wtedy wystarczy znaleźć odpowiednie równanie przeliczania liczb na indeksy.

from random import randint


def count_sort(A, k):
    C = [0]*k
    B = [0]*len(A)
    for x in range(len(A)):
        C[A[x]] += 1
    for x in range(1, k):
        C[x] += C[x-1]
    for x in range(len(A)-1, -1, -1):
        B[C[A[x]]-1] = A[x]
        C[A[x]] -= 1
    for x in range(len(A)):
        A[x] = B[x]
    return A


n = 10
tab = [randint(0, n-1) for x in range(n)]
n = len(tab)
print(tab)
print(count_sort(tab, n))
