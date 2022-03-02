# One approach is to use hashing and second one is to use sorting.

# O(n)
def ex001_1(tab, k):
    d, n = {}, len(tab)
    for x in range(n):
        if k-tab[x] in d:
            return True
        d[tab[x]] = True
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


# O(n log n)
def ex001_2(tab, k):
    n = len(tab)
    tab.sort()
    for x in range(n):
        if binary_search(tab, k-tab[x]):
            return True
    return False


tab = [1, 4, 5, 10]
print(ex001_2(tab, 14))
