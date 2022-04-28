# Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
# jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
# (1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.
#
#
# Zakładam, że startujemy z pełnym bakiem (gdyby było inaczej, problem jest analogiczny). Mam w baku L litrów paliwa.
# Patrzę więc na indeks tablicy L do przodu i sprawdzam, czy jest tam stacja. Jeżeli jest to tam jadę i tankuję do
# pełna. Jeżeli nie to przesuwam się do tyłu i sprawdzam najbliższą stację, a więc najdalszą od naszego punktu
# startowego, do której mogę dojechać i do niej się udaję. Jeżeli po drodze nie będzie żadnych stacji, to nie
# istnieje poprawne rozwiązanie. Powtarzam te operacje do momentu dotarcia do miejsca docelowego lub stwierdzenia,
# że nie ma takiej możliwości.
# Złożoność obliczeniowa: O(n)

def travel(tab, L, p):
    ctr = 0
    aux_tab = [False]*(p+1)
    for x in range(len(tab)):
        aux_tab[tab[x]] = True
    ctr1 = 0
    max_ctr = 0
    while True:
        ctr += L
        if ctr >= p:
            return max_ctr
        while True:
            if ctr == ctr1:
                return False
            if aux_tab[ctr] is True:
                ctr1 = ctr
                max_ctr += 1
                break
            ctr -= 1


tab = [2, 4, 6, 8]
print(travel(tab, 2, 9))
