# O(n * log(log(n))) + log(n)*log(n)*(log(log(n))))
# n > (log(n))^2
# so O(n log(log n))
def binary_search(tab, k):
    n = len(tab)
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if tab[m][0] == k:
            return m
        elif tab[m][0] > k:
            r = m - 1
        else:
            l = m + 1
    return False


def quick_sort(tab, p, r):
    while p < r:
        q = partition(tab, p, r)
        quick_sort(tab, p, q-1)
        p = q + 1
    return tab


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


def ex02(tab):
    n = len(tab)
    aux_tab = [(10**10, 10**10)] * 4
    for x in range(n):
        sol = binary_search(aux_tab, tab[x])
        if sol is not False:
            aux_tab[sol] = (aux_tab[sol][0], aux_tab[sol][1]+1)
        else:
            aux_tab[len(aux_tab)-1] = (tab[x], 1)
            quick_sort(aux_tab, 0, len(aux_tab)-1)
    ctr = 0
    for x in range(len(aux_tab)):
        for y in range(aux_tab[x][1]):
            tab[ctr] = aux_tab[x][0]
            ctr += 1
    return tab


tab = [30, 20, 30, 30, 40, 10, 20, 10, 10, 20, 40]
print(ex02(tab))
