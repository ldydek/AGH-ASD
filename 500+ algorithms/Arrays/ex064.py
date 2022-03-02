# O(n)
def ex064(tab):
    n, ctr = len(tab), 0
    k = sum(tab)
    s1, s2 = [], []
    k = k // 2
    for x in range(n):
        if ctr != k:
            s1.append(tab[x])
            ctr += tab[x]
        else:
            s2.append(tab[x])
    return s1, s2


tab = [6, -4, 3, -3, 2]
print(ex064(tab))
