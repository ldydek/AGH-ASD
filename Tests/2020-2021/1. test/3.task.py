# Number distribution in the entire range is not uniform, but we are guaranteed that within unitry interval it is. 
# So we can divide this range to "n" interval and in each interval sort elements with bucket sort. At the end, we merge
# all unitry intervals.
# Time complexity: O(n)
# Space complexity: O(n)
# Passed all tests


def insertion_sort(tab):
    n = len(tab)
    for x in range(1, n):
        k = tab[x]
        y = x - 1
        while y >= 0 and k < tab[y]:
            tab[y+1], tab[y] = tab[y], tab[y+1]
            y -= 1
    return tab


def bucket_sort(tab, mini):
    n = len(tab)
    buckets = [[] for _ in range(n+1)]
    interval = 1 / n
    for x in range(len(tab)):
        buckets[int((tab[x]-mini-1)/interval)].append(tab[x])
    for x in range(len(buckets)):
        insertion_sort(buckets[x])
    ctr = 0
    for x in range(len(buckets)):
        for y in range(len(buckets[x])):
            tab[ctr] = buckets[x][y]
            ctr += 1
    return tab


def SortTab(T, P):
    n = len(T)
    aux_tab = [[] for _ in range(n)]
    for x in range(n):
        aux_tab[int(T[x]) - 1].append(T[x])
    for x in range(len(aux_tab)):
        if len(aux_tab[x]) > 0:
            bucket_sort(aux_tab[x], x)
    ctr = 0
    for x in range(len(aux_tab)):
        for y in range(len(aux_tab[x])):
            T[ctr] = aux_tab[x][y]
            ctr += 1
    return T


T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.1, 7.8]
P = [(1, 5, 0.75), (4, 8, 0.25)]
print(SortTab(T, P))
