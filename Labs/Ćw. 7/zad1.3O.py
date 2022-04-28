# Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
# jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
# Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo
# cenę za litr paliwa). Jeżeli tankujemy na stacji, to do pełna.


# Podejście dynamiczne:
# f(i) - minimalny koszt, aby dojechać na pole i, tankując zawsze do pełna
# f(i) = min(f(i-v) + (i-v)*P[i]); i-v>0 a P to tablica zawierająca ceny paliwa za litr w danym miejscu
# rozw. f(n-1)
# dla przypadku cen paliw
# P = [10, 30, 31, 30]
# L = 2 a koniec podróży w 4
# algorytm dynamiczny wybierze tankowanie 2 litrów w 31 i razem mamy 10*2 + 2*31=82
# a zachłanny najpierw pierwszą 30 bo jest najtańsza, a potem drugą 30, tankując do pełna
# 30+2*30=90, więc nie znajdzie optymalnego rozwiązania.
from math import inf


def travel(tab, L):
    n = len(tab)
    aux_tab = [0]*n
    aux_tab[0] = tab[0]*L
    for x in range(1, n):
        ctr = inf
        for y in range(x):
            if x-y <= L:
                ctr = min(ctr, aux_tab[y] + (x-y)*tab[x])
        aux_tab[x] = ctr
    return aux_tab[n-1]


tab = [10, 30, 31, 30, 0]
L = 2
print(travel(tab, L))

