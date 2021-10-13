# Złożoność obliczeniowa: O(n^2)
# Z każdą iteracją pętli wewnętrznej wybieramy aktualnie najmniejszy element pozostałego podciągu do posortowania
# i wstawiamy go w odpowiednie miejsce w tablicy.

from random import randint


def fun(tab):
    if len(tab) == 1:
        return tab
    else:
        for x in range(len(tab)):
            k = x
            for y in range(x, len(tab)):
                if tab[y] < tab[k]:
                    k = y
            tab[x], tab[k] = tab[k], tab[x]
    return tab


tab = [randint(1, 15) for _ in range(5)]
print(tab)
print(fun(tab))
