# Sortowanie przez wstawianie
# Złożoność czasowa: O(n^2)
# Idealnie nadaje się do posortowania małej ilości danych np. elementów w kubełkach w sortowaniu kubełkowym
# albo zbiorów pięcioelementowych w algorytmie magicznych piątek.
from random import randint


def insertion_sort(tab):
    if len(tab) == 1:
        return tab
    else:
        for x in range(1, len(tab)):
            key = tab[x]
            y = x - 1
            while y >= 0 and tab[y] > key:
                tab[y+1] = tab[y]
                y = y - 1
            tab[y+1] = key
    return tab


tab = [randint(1, 30) for _ in range(8)]
print(tab)
print(insertion_sort(tab))
