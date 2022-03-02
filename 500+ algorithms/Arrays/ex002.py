# O(n)
def ex002(tab):
    n, d = len(tab), set()
    d.add(0)
    for x in range(1, n):
        tab[x] += tab[x-1]
    for x in range(n):
        if tab[x] in d:
            return True
        d.add(tab[x])
    return False


tab = [3, 4, -7, 3]
print(ex002(tab))
