# [ENG] In radix sort algorithm we use counting sort algorithm several times to sort, for instance, triple digit
# numbers or words. We start sorting numbers from the least important digit (located at the end of the number) to the
# most important. Algorithm is stable, but doesn't work in place.
# Time complexity: θ(d(n+k)), where "d" is the length of numbers and "k" is the range of digits
# If "d" is constant and k=O(n) algorithm works in linear time.
# [PL] Algorytm sortowania pozycyjnego opiera się na wywoływaniu kilkukrotnie algorytmu sortowania przez zliczanie,
# zaczynając od najmniej znaczącej cyfry a kończąc na tej najbardziej znaczącej. Jest on stabilny, lecz nie działa
# w miejscu.
# Złożoność czasowa: θ(d(n+k)), gdzie "d" jest ilością cyfr w liczbach a "k" zakresem występowania tych liczb.
# Jeśli "d" jest stałą a k=O(n), to sortowanie działa w czasie liniowym.

def radix_sort(A, d):
    n = len(A)
    B = [0]*n
    for b in range(d):
        C = [0]*10
        for x in range(n):
            digit = (A[x]//10**b) % 10
            C[digit] += 1
        for x in range(1, 10):
            C[x] += C[x-1]
        for x in range(n-1, -1, -1):
            B[C[(A[x]//10**b) % 10]-1] = A[x]
            C[(A[x]//10**b) % 10] -= 1
        for x in range(n):
            A[x] = B[x]
    return A


tab = [329, 457, 657, 839, 436, 720, 355]
print(radix_sort(tab, 3))
