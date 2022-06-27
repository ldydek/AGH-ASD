def ex01(tab):
    n = len(tab)
    for x in range(n):
        for y in range(n-1):
            if tab[y] > tab[y+1]:
                tab[y], tab[y+1] = tab[y+1], tab[y]
    return tab


tab = [10, 2, 13, 56, 14]
print(ex01(tab))
