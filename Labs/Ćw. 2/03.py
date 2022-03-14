# [ENG] Looking for two elements with a certain sum in a sorted array.
# [PL] Szukanie dwóch elementów o określonej sumie w posortowanej tablicy.
# O(n)

def ex03(tab, k):
    n = len(tab)
    a, b = 0, n-1
    while a <= b:
        if tab[a] + tab[b] > k:
            b -= 1
        elif tab[a] + tab[b] < k:
            a += 1
        else:
            return True
    return False


tab = [1, 3, 5, 6, 10, 15, 17]
print(ex03(tab, 34))
