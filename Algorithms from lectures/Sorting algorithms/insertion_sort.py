# [ENG] In insertion sort algorithm we start sorting array from second element (when array has only one element for loop
# won't execute and function will simply return array without any modification) and for that element we look its
# suitable place in the subarray from tab[0] to tab[x-1] where x is our element we consider (at the beginning it'll be
# x = 1 (second element).
# Time complexity: O(n^2)
# [PL] W algorytmie sortowania przez wstawianie rozpoczynamy sortowanie tablicy od drugiego elementu (jeśli tablica
# posiada tylko jeden element, to pętla for w ogóle się nie wykona i funkcja po prostu zwróci przekazaną tablicę) i dla
# niego szukamy odpowiedniego miejsca w podtablicy od tab[0] do tab[x-1], gdzie x jest obecnie rozważanym elementem
# (na początku x=1, czyli drugi element).
# Złożoność czasowa: O(n^2)


def insertion_sort(tab):
    n = len(tab)
    for x in range(1, n):
        # [ENG] "key" is element for which we are looking for suitable place in the subarray
        # [PL] "key" jest elementem tablicy, dla którego szukamy odpowiedniego miejsca w danej podtablicy
        key = tab[x]
        y = x - 1
        while y >= 0 and tab[y] > key:
            tab[y+1] = tab[y]
            y = y - 1
        tab[y+1] = key
    return tab


tab = [3, 2, 17, 1, 10, 5, 13, 6]
print(insertion_sort(tab))
