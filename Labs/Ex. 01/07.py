# [ENG] For each element in an array we look for k-A[j] element using binary search.
# Time complexity: O(n lg n)
# [PL] Dla każdego elementu w tablicy za pomocą wyszukiwania binarnego szukamy elementu k-A[j].
# Time complexity: O(n lg n)

def ex07(tab, k):
    n = len(tab)
    for x in range(n):
        if binary_search(tab, k-tab[x]):
            return True
    return False


def binary_search(tab, k):
    n = len(tab)
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if tab[m] == k:
            return m
        elif tab[m] > k:
            r = m - 1
        else:
            l = m + 1
    return False


tab = [1, 3, 4, 6, 9, 10, 13, 15]
print(ex07(tab, 26))
