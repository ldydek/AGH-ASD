# Sortowanie szybkie. Często i chętnie stosowane w celu posortowania danych. Na początku wybieramy piwota i elementy
# mniejsze lub równe znajdują się na lewo od niego, a większe na prawo po wywołaniu funkcji partition.
# W przeciwieństwie do merge sorta po zejściu rekurencyjnym od razu otrzymujemy posortowany ciąg danych bez
# potrzeby ich scalania.
# Złożoność obliczeniowa: O(n lgn)
from random import randint


def quick_sort(tab, p, r):
    while p < r:
        q = partition(tab, p, r)
        quick_sort(tab, p, q-1)
        p = q + 1
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


tab = [randint(0, 20) for _ in range(13)]
print(tab)
n = len(tab)
print(quick_sort(tab, 0, n-1))
