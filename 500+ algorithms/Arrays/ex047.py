def ex047(tab):
    n, ctr = len(tab), 0
    mini = -10**10
    solution = 1
    for x in range(n):
        if tab[x] < 0:
            ctr += 1
            mini = max(mini, tab[x])
    for x in range(n):
        if tab[x] != 0:
            solution *= tab[x]
    if ctr % 2:
        solution //= mini
    return solution


tab = [-6, 4, -5, 8, -10, 0, 8]
print(ex047(tab))
