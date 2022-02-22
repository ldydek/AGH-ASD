def ex021(tab):
    n, ctr = len(tab), 0
    for x in range(n):
        if tab[x] == 0:
            ctr += 1
    tab[0:ctr], tab[ctr:n] = [0]*ctr, [1]*(n-ctr)
    return tab


tab = [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
print(ex021(tab))
