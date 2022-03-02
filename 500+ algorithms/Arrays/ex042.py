def ex042(tab):
    n = len(tab)
    a, b = None, None
    for x in range(1, n):
        if a and tab[x-1] > tab[x]:
            b = x
        if tab[x-1] > tab[x] and not a:
            a, b = x-1, x
    tab[a], tab[b] = tab[b], tab[a]
    return tab


tab = [3, 5, 6, 13, 10, 22, 24]
print(ex042(tab))
