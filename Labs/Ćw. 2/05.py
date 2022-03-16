def ex05(tab):
    n = len(tab)
    leader, ctr = tab[0], 0
    for x in range(n):
        if leader == tab[x]:
            ctr += 1
        else:
            ctr -= 1
        if ctr < 0:
            leader = tab[x]
            ctr = 0
    ctr = 0
    for x in range(n):
        if tab[x] == leader:
            ctr += 1
    if ctr > n//2:
        return True
    return False


tab = [1, 1, 2, 10, 3, 1]
print(ex05(tab))
