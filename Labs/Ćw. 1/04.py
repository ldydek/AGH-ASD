def ex04(tab):
    n = len(tab)
    minimum, maximum = 10*10, -10**10
    for x in range(2-n % 2, n, 2):
        a, b = min(tab[x], tab[x+1]), max(tab[x], tab[x+1])
        minimum = min(minimum, a)
        maximum = max(maximum, b)
    minimum = min(minimum, tab[0])
    maximum = max(maximum, tab[0])
    return minimum, maximum


tab = [2, 10, 4, 7, -4, 300, 40, 5]
print(ex04(tab))
