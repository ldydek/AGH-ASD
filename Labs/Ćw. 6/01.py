# Pomiędzy dwoma drzewa do ścięcia musi zostać minimalnie jedno drzewa, którego nie zetniemy i maksymalnie dwa,
# ponieważ gdyby były trzy, to drzewo środkowe można ściąć nie naruszając warunków zadania.
# f(i) - maksymalny koszt przy ścięciu drzew na pozycjach od tab[0] do tab[i] włącznie
# f(i) = max(f(i-2)+tab[i], f(i-1))
# Pomiędzy dwoma drzewa do ścięcia musi zostać minimalnie jedno drzewa, którego nie zetniemy i maksymalnie dwa,
# ponieważ gdyby były trzy, to drzewo środkowe można ściąć nie naruszając warunków zadania.
# f(i) - maksymalny koszt przy ścięciu drzew na pozycjach od tab[0] do tab[i] włącznie
# f(i) = max(f(i-2)+tab[i], f(i-1))
# f(0) = tab[0]
# f(1) = max(tab[0], tab[1])
# albo dane drzewo ścinamy i rekurencyjnie wywołujemy się na zbiorze o 2 mniejszym, albo dane drzewo zostawiamy
# wywołujemy się rekurencyjnie na zbiorze o 1 mniejszym
# czas: O(n)
# pamięć: w miejscu


def ex01(tab):
    n = len(tab)
    x1, x2 = tab[0], max(tab[0], tab[1])
    for x in range(2, n):
        x1, x2 = x2, max(x1+tab[x], x2)
    return x2


tab = [100, 27, 8, 9, 13]
print(ex01(tab))
