# [ENG] Quicksort without recursion (with own stack).
# [PL] Sortowanie szybkie bez rekursji (z własnym stosem).

def ex03(tab, p, r):
    stack = [(p, r)]
    while stack:
        p, r = stack.pop()
        q = partition(tab, p, r)
        if p < q - 1:
            stack.append((p, q-1))
        if q + 1 < r:
            stack.append((q+1, r))
    return tab


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


tab = [2, 1, 15, 34, 20, 3, 6, 78]
print(ex03(tab, 0, len(tab)-1))
