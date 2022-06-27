def merge(tab, aux_tab, p, q):
    ctr = p
    xd1, xd2 = p, q
    while xd2 != q+1:
        if tab[xd1] < tab[xd2]:
            aux_tab[ctr] = tab[xd1]
            xd1 += 1
        else:
            aux_tab[ctr] = tab[xd2]
            xd2 += 1
        ctr += 1

    while xd1 < q and xd2 < len(tab) and tab[xd2-1] < tab[xd2]:
        if tab[xd1] < tab[xd2]:
            aux_tab[ctr] = tab[xd1]
            xd1 += 1
        else:
            aux_tab[ctr] = tab[xd2]
            xd2 += 1
        ctr += 1

    while xd1 < q:
        aux_tab[ctr] = tab[xd1]
        ctr += 1
        xd1 += 1
    while xd2 < len(tab) and tab[xd2] > tab[xd2-1]:
        aux_tab[ctr] = tab[xd2]
        ctr += 1
        xd2 += 1
    for x in range(p, xd2):
        tab[x] = aux_tab[x]
    return xd2


def ex01_a(tab):
    n = len(tab)
    aux_tab = [0] * n
    sorted = False
    while sorted is False:
        p, q = 0, None
        sorted = True
        x = 1
        while x < n:
            if q is None and tab[x-1] > tab[x]:
                sorted = False
                q = x
                p = merge(tab, aux_tab, p, q)
                x = p
                q = None
            x += 1
    return tab


tab = [0, 1, 27, 1, 5, 7, 3, 4, 100, 123, 1, 2, 3, 2, 3]
print(ex01_a(tab))
