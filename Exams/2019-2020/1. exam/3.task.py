# Firstly, we have to from the function values get to its arguments, so we are forced to logarithm every number. Now
# we run bucket sort algorithm, because function arguments come from uniform distribution. After sorting all the numbers
# we back to function values, because exponential function a^x, where a > 1 is always an increasing function.
# Time complexity: O(n)
# Space complexity: O(n)
# Passed all tests

from math import log


def insertion_sort(tab):
    n = len(tab)
    for x in range(1, n):
        key = tab[x]
        y = x - 1
        while y >= 0 and tab[y] > key:
            tab[y+1] = tab[y]
            y = y - 1
        tab[y+1] = key
    return tab


def bucket_sort(tab):
    n = len(tab)
    buckets = [[] for _ in range(n)]
    interval = 1/n
    for x in tab:
        buckets[int(x//interval)].append(x)
    index = 0
    for x in range(n):
        if len(buckets[x]) > 0:
            insertion_sort(buckets[x])
        for y in buckets[x]:
            tab[index] = y
            index += 1
    return tab


def fast_sort(tab, a):
    n = len(tab)
    for x in range(n):
        tab[x] = log(tab[x], a)
    bucket_sort(tab)
    for x in range(n):
        tab[x] = a ** tab[x]
    return tab


T = [0.1, 0.5, 0.2, 0.78, 0.01]
print(fast_sort(T, 2))
