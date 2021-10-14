# [ENG] Bubble sort algorithm. In each iteration internal loop two neighbouring elements are compared and possibly
# swapped. "N" iterations of the external loop is necessary if the least element is located at the end of the list.
# Time complexity: O(n^2)
# [PL] Sortowanie bąbelkowe. Elementy w każdej iteracji pętli wewnętrznej są porównywane i gdy element na lewo jest
# większy od tego na prawo, to są one zamieniane miejscami. W pesymistycznym przypadku najmniejszy element będzie na
# samym końcu tablicy do posortowania, a zatem po wykonaniu "n" razy pętli zewnętrznej na pewno otrzymamy posortowaną
# tablicę.
# Złożoność czasowa: O(n^2)

def bubble_sort(tab):
    n = len(tab)
    for x in range(n):
        for y in range(n-1):
            # [ENG] if element located on the right is smaller it is swapped with currently considered element
            # [PL] jeśli element położony na prawo jest mniejszy od obecnie rozważanego, to zostają one zamienione
            if tab[y] > tab[y+1]:
                tab[y], tab[y+1] = tab[y+1], tab[y]
    return tab


# [ENG] Optimised version of the bubble sort algorithm. Note that after each iteration of the internal loop at the
# end of our list some numbers are already sorted. After first iteration the biggest number is at the end, so on its
# appropriate place. After second iteration second biggest number is on its suitable place and so on. This trick will
# reduce number of operations, but time complexity is still O(n^2) - in pessimistic case.
# [PL] Zoptymalizowana wersja sortowania bąbelkowego. Warto tutaj zauważyć, iż po każdej iteracji na końcu tablicy
# tworzy się podzbiór elementów już posortowanych. Po pierwszej będzie to największa liczba, po drugiej będzie to 
# druga największa liczba itd. Ta sztuczka pozwoli zredukować ilość operacji, lecz złożoność algorytmu zostaje nadal
# O(n^2) - z dokładnością do stałej.

def optimised_bubble_sort(tab):
    n = len(tab)
    for x in range(n):
        p = True
        # [ENG] "p" variable will inform if list is finally sorted. If so, algorithm finishes.
        # [PL] zmienna "p" będzie informować, czy lista jest już posortowana. Jeśli tak, to algorytm kończy działanie.
        for y in range(n-1-x):
            if tab[y] > tab[y+1]:
                tab[y], tab[y+1] = tab[y+1], tab[y]
                p = False
        if p:
            break
    #     [ENG] "if p" is the same as "if p is True" or "if p == True"
    #     [PL] "if p" to to samo co "if p is True" lub "if p == True"
    return tab

tab = [10, 2, 13, 56, 14]
print(bubble_sort(tab))
