# [ENG] Dividing a list in quicksort according to Hoare's idea.
# [PL] Dzielenie tablicy w sortowaniu szybkim wg pomysłu Hoare'a

def ex07(tab, p, r):
    while p < r:
        q = partition(tab, p, r)
        ex07(tab, p, q-1)
        p = q + 1
    return tab


def partition(tab, p, r):
    x = r
    r -= 1
    while p < r:
        if tab[p] > tab[x] > tab[r]:
            tab[p], tab[r] = tab[r], tab[p]
        if tab[p] > tab[x]:
            while tab[r] > tab[x]:
                r -= 1
            tab[p], tab[r] = tab[r], tab[p]
        if tab[r] < tab[x]:
            while tab[p] < tab[x]:
                p += 1
            tab[p], tab[r] = tab[r], tab[p]
        p += 1
        r -= 1
    tab[x], tab[p] = tab[p], tab[x]
    return p


tab = [3, 1, 5, 8, 2, 7, 10, 5]
print(ex07(tab, 0, len(tab)-1))
