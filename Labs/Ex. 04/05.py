# O(n)
def ex05_g(tab, k):
    n = len(tab)
    solution = 10 ** 10
    aux_tab = [0] * k
    ctr = 0
    i = 0
    a, b = None, None
    for x in range(n):
        if aux_tab[tab[x]] == 0:
            ctr += 1
        aux_tab[tab[x]] += 1
        if ctr == k:
            if solution > x - i:
                solution = x - i
                a, b = i, x
            while ctr == k:
                if solution > x - i:
                    solution = x - i
                    a, b = i, x
                aux_tab[tab[i]] -= 1
                if aux_tab[tab[i]] == 0:
                    ctr -= 1
                i += 1
    return a, b


k = 4
tab = [1, 1, 2, 1, 1, 3, 1, 0, 1, 2]
print(ex05_g(tab, k))
