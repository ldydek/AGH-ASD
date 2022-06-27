def ex04(tab):
    n = len(tab)
    if n == 1:
        return tab[0], tab[0]
    if n % 2 == 0:
        minimum = min(tab[0], tab[1])
        maximum = max(tab[0], tab[1])
    else:
        minimum = tab[0]
        maximum = tab[0]
    for x in range(2-n % 2, n, 2):
        a, b = min(tab[x], tab[x+1]), max(tab[x], tab[x+1])
        minimum = min(minimum, a)
        maximum = max(maximum, b)
    return minimum, maximum


tab = [2, 10, 4, 7, -40, 300, 40, 5]
print(ex04(tab))
