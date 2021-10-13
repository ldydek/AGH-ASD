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


tab = [10, 2, 13, 56, 14]
print(bubble_sort(tab))
