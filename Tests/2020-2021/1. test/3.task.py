def insertion_sort(tab):
    n = len(tab)
    for x in range(1, n):
        k = tab[x]
        y = x - 1
        while y >= 0 and k < tab[y]:
            tab[y+1], tab[y] = tab[y], tab[y+1]
            y -= 1
    return tab


def bucket_sort(buckets, tab):
    for x in range(len(buckets)):
        buckets[x] = []
    for x in range(len(tab)):
        buckets[int(tab[x] * 10) % 10].append(tab[x])
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
    buckets = [[] for _ in range(10)]
    for x in range(n):
        aux_tab[int(T[x]) - 1].append(T[x])
    for x in range(len(aux_tab)):
        bucket_sort(buckets, aux_tab[x])
    ctr = 0
    for x in range(len(aux_tab)):
        for y in range(len(aux_tab[x])):
            T[ctr] = aux_tab[x][y]
            ctr += 1
    return T


T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.1, 7.8]
P = [(1, 5, 0.75), (4, 8, 0.25)]
print(SortTab(T, P))

