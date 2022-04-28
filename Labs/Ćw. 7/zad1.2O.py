# Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
# jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
# Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo cenę
# za litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.
#
#
# Jestem na danej stacji z pewną ilością paliwa. Jeżeli w odległości L od tej stacji (bo tyle mogę maksymalnie
# przejechać tankując na tej stacji do pełna) jest jakaś stacja z tańszą ceną, to tankuję minimalną ilość paliwa,
# która pozwoli mi do niej dojechać (być może 0). Natomiast jeśli nie ma tańszej w odległości L, to tankuję na obecnej
# stacji do pełna i jadę do najtańszej stacji dalej (która ma droższą cenę od obecnej stacji).
# Implementacja niedokończona.
from math import inf


def travel(tab, L):
    n = len(tab)
    solution = 0
    station1, station2 = 0, 0
    t = inf
    k = 0
    while k < n:
        k = station2
        for x in range(L):
            solution += tab[k]
            station1 += 1
            if station1 < n and tab[station1] <= t:
                t = tab[station1]
                station2 = station1
                if t < tab[k]:
                    break
    return solution






tab = [10, 30, 31, 30]
L = 2
print(travel(tab, L))