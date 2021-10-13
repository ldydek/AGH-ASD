# [ENG] In selection sort algorithm we choose in each iteration of the internal loop the smallest element from the
# remaining subarray and after that we swap this element from the first element of our considered subarray.
# Time complexity: O(n^2)
# [PL] W algorytmie sortowanie przez wybieranie z każdą iteracją pętli wewnętrznej wybieramy aktualnie najmniejszy
# element pozostałej podtablicy do posortowania i wstawiamy go na pierwsze miejsce rozważanej podtablicy.
# Złożoność obliczeniowa: O(n^2)

def selection_sort(tab):
    n = len(tab)
    for x in range(n):
        k = x
        # [ENG] "x" is the index of first element of remaining subarray to sort. Elements from tab[0] to tab[x] are
        # already sorted.
        # [PL] "x" jest indeksem pierwszego elementu pozostałej podtablicy do posortowania. Elementy od tab[0] do
        # tab[x] są już posortowane.
        for y in range(x, n):
            if tab[y] < tab[k]:
                k = y
        tab[x], tab[k] = tab[k], tab[x]
    return tab


tab = [10, 3, 2, 67, 23, 100, 4]
print(selection_sort(tab))
