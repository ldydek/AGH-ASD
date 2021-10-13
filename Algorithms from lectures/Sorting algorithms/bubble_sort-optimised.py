# [ENG] Optimised version of the bubble sort algorithm. If you want to know, what this algorithm does check notes
# in bubble_sort file. Note that after each iteration of the internal loop at the end of our list some numbers are
# already sorted. After first iteration the biggest number is at the end, so on its appropriate place. After second
# iteration second biggest number is on its suitable place and so on. This trick will reduce number of operations, but
# time complexity is still O(n^2) - in pessimistic case.
# [PL] Zoptymalizowana wersja sortowania bąbelkowego. Jeśli chcesz się dowiedzieć, jak działa ten algorytm, to odsyłam
# do notatek w pliku bubble_sort. Warto tutaj zauważyć, iż po każdej iteracji na końcu tablicy tworzy się
# podzbiór elementów już posortowanych. Po pierwszej będzie to największa liczba, po drugiej będzie to druga największa 
# liczba itd. Ta sztuczka pozwoli zredukować ilość operacji, lecz złożoność algorytmu zostaje nadal O(n^2)
# - z dokładnością do stałej.

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
    #     "if p" is the same as "if p is True" or "if p == True"
    return tab


tab = [10, 1, 13, 5, 16, 30, 23, 200, 34]
print(optimised_bubble_sort(tab))
