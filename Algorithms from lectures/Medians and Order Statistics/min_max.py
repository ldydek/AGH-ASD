# [ENG] To find minimum and maximum in an unsorted array we can just traverse whole array and find that elements in
# linear time. It's important to note that in this way we make two comparisons for one element, because we compare each
# element with temporary minimum and maximum. True is we can find that elements making less comparisons. Idea is to
# compare two neighbouring elements with each other and later larger with maximum and smaller with minimum. Thanks to
# this trick we make 3 comparisons for every 2 elements.
# Time complexity: O(n)
# [PL] Aby znależć zarówno minimum jak i maksimum w nieposortowanej tablicy danych możemy po prostu dwa razy całą tę
# tablicę przejrzeć. Wykonujemy wtedy dla każdego elementu dwa porównania z tymczasowym minimum i maksimum. Prawda jest
# jednak taka, że aby te elementy wyznaczyć wytarczą 3 porównania na 2 elementy. Pomysł jest następujący: na początku
# dwa sąsiednie elementy tablicy porównujemy ze sobą nawzajem a potem większy z nich z maksimum a mniejszy z minimum.
# Złożoność obliczeniowa: O(n)

def min_max(tab):
    n = len(tab)
    if n == 1:
        return tab[0], tab[0]
    if n % 2 == 0:
        minimum = min(tab[0], tab[1])
        maximum = max(tab[0], tab[1])
    else:
        minimum = tab[0]
        maximum = tab[0]
    for x in range(2-n % 2, n, 2):
        a, b = min(tab[x], tab[x+1]), max(tab[x], tab[x+1])
        minimum = min(minimum, a)
        maximum = max(maximum, b)
    return minimum, maximum


tab = [2, 10, 4, 7, -4, 300, 40, 5]
print(min_max(tab))

# [ENG] Whole number of comparisons is not more than 3*(n//2)
# [PL] Całkowita ilość porównań nie przekracza 3*(n//2)
