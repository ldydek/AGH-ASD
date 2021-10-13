# [ENG] In quick sort algorithm at the beginning we choose a pivot (one of array elements and according to this element we
# will be modifying array - smaller or equal numbers than pivot will be on the left and greater on the right). This is
# happening in a "partition" function. Later, we recursively do the same thing for two subarrays and pivot is this
# element which divide this two subarrays. When recursion finishes array is sorted.
# In average case height of recursion tree will be O(lg n) and in the same level of the tree we have O(n) elements.
# Seldom will time complexity O(n^2) happen.
# Time complexity: O(n lg n)
# [PL] W sortowaniu szybkim na początku wybieramy piwota (jeden z elementów tablicy i elementy mniejsze lub równe znajdą
# się na lewo od niego, a większe na prawo po modyfikacji tablicy w funkcji "partition"). Rekurencyjnie wywołujemy
# funkcję dla dwóch podtablic i tę operację powtarzamy do momentu końca rekursji. Po zakończeniu tablica jest
# posortowana.
# W przeciętnym przypadku wysokość drzewa rekursji będzie rzędu O(lg n) a na każdym poziomie będziemy mieć O(n)
# elementów. Złożoność O(n^2) bardzo rzadko ma miejsce.
# Złożoność obliczeniowa: O(n lg n)

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


tab = [2, 5, 10, 1, 7, 40, 6, 6]
print(quick_sort(tab, 0, len(tab)-1))
