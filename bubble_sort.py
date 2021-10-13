# Bubble sort algorithm. In each iteration internal loop two neighbouring elements are compared and possibly swapped.
# "N" iterations of the external loop is necessary if the least element is located at the end of the list.
def bubble_sort(tab):
    n = len(tab)
    for y in range(n):
        for x in range(y):
            # if element located on the right is smaller it is swapped with currently considered element
            if tab[x] > tab[x+1]:
                tab[x], tab[x+1] = tab[x+1], tab[x]
    return tab


tab = [10, 1, 13, 5, 16, 30, 23]
print(bubble_sort(tab))
