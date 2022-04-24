# Idea is to sort given array and after this check how far from the starting position is every element after sorting.
# But not every sorting algorithm is good here - it has to be stable. So we could use here mergesort or quicksort, but
# before doing quicksort we have to make a small preprocessing. If we don't sort single numbers but rather tuples:
# (number, its starting position), we'll obtain stable sorting, because in python tuple (2,3) is smaller than (2,5), so,
# for instance, number 2 in starting index 3 after sorting will be before number 2 in starting index 5. At the end, we
# have to find maximum difference between starting position and current position and this will be a solution.
# Time complexity: O(n log n)
# Space complexity: O(n)
# Passed all tests

from math import inf


def partition(tab, p, r):
    tab[r], tab[(p+r)//2] = tab[(p+r)//2], tab[r]
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


def quick_sort(tab, p, r):
    while p < r:
        q = partition(tab, p, r)
        quick_sort(tab, p, q-1)
        p = q + 1


def chaos_index(T):
    for x in range(len(T)):
        T[x] = (T[x], x)
    quick_sort(T, 0, len(T)-1)
    sol = -inf
    for x in range(len(T)):
        sol = max(sol, abs(x-T[x][1]))
    return sol


tab = [0, 2, 1.1, 2]
print(chaos_index(tab))
