# [ENG] In counting sort algorithm we don't make any comparisons between elements. That's why if data to sort is
# specific (integer numbers and from small range) we can do that operation in linear time. All we need to do is to
# allocate two additional arrays: in the first one (called C) we store information how many elements are less or equal
# to "i" and we can find that in C[i]. Second one we use simply to rewrite elements and get solution.
# Note that negative integer numbers are also acceptable - then we have to find equation converting numbers to indexes.
# Counting sort is stable!
# Time complexity: O(n+k) where k is the range of numbers to sort. If k = O(n) time complexity is θ(n).
# [PL] W algorytmie sortowania przez zliczanie nie dokonujemy żadnych porównań między elementami, dlatego jesteśmy
# w stanie posortować daną tablicę dla specyficznych danych (liczby całkowite z małego zakresu) w czasie liniowym.
# Alokujemy dwie pomocnicze tablice. Pierwsza z nich (nazwana C) służy do przechowywania informacji - dla elementu
# C[i] wiemy, ile liczb jest mniejszych lub równych i. W tablicy B przechowujemy posortowaną tablicę.
# Złożoność obliczeniowa: O(n+k), gdzie k jest zakresem liczb do posortowania. Jeśli k = O(n), to posortowanie
# zajmie θ(n). Algorytm jest stabilny! Liczby ujemne też mogą wystąpić i wtedy wystarczy znaleźć odpowiednie równanie
# przeliczania liczb na indeksy.

def count_sort(A, k):
    n = len(A)
    C = [0]*k
    B = [0]*n
    for x in range(n):
        C[A[x]] += 1
    for x in range(1, k):
        C[x] += C[x-1]
    for x in range(n-1, -1, -1):
        B[C[A[x]]-1] = A[x]
        C[A[x]] -= 1
    # [ENG] C[A[x]] -= 1 is necessary if elements are not distinct
    # [PL] C[A[x]] -= 1 jest konieczne jeśli elementy nie są parami różne
    return B


def count_sort_negative_numbers(A):
    n, a, b = len(A), min(A), max(A)
    k = b-a+1
    # [ENG] "k" is range of numbers
    # [PL] "k" jest zakresem występowania liczb
    C = [0]*k
    B = [0]*n
    for x in range(n):
        C[A[x]-a] += 1
    for x in range(1, k):
        C[x] += C[x-1]
    for x in range(n-1, -1, -1):
        B[C[A[x]-a]-1] = A[x]
        C[A[x]-a] -= 1
    return B


tab = [7, 3, 5, 5, 1, 2, 1, 5, 4, 7, 3]
n = 8
print(count_sort(tab, n))
