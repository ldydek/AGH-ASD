# [ENG] To find kth smallest element in an unsorted array I use "partition" function from e.g. quicksort. Then, if
# pivot is exactly kth smallest element I can simply return it. We know that, because after partition elements smaller
# are on the left and greater on the right (numbers are distinct). Otherwise, we are forced to call a function
# recursively either on the left part or right. It depends on the fact if kth smallest element is greater than our pivot
# or not.
# [PL] Do znalezienia "k-tego" najmniejszego elementu w nieposortowanej tablicy używam funkcji "partition" np. z
# algorytmu sortowania szybkiego. Następnie jeśli piwot jest dokładnie "k-tym" najmniejszym elementem mogę go po prostu
# zwrócić, ponieważ mamy pewność, że liczby na lewo od piwota są mniejsze, a na prawo większe oraz elementy są parami
# różne. Natomiast jeśli tak nie jest funkcja zostaje wywołana rekurencyjnie na lewej bądź prawej części w zależności
# od tego czy piwot jest mniejszy od "k-tego" elementu czy większy.
# [ENG] Expected time complexity: O(n), pessimistically: O(n^2)
# [PL] Oczekiwana złożoność czasowa: O(n), pesymistycznie: O(n^2)

def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


def quick_select(tab, p, r, i):
    if p == r:
        return tab[p]
    q = partition(tab, p, r)
    k = q - p + 1
    if k == i:
        return tab[q]
    elif k < i:
        return quick_select(tab, q+1, r, i-k)
    else:
        return quick_select(tab, p, q-1, i)


tab = [3, 1, 7, 6, 2, 10, 13, 5]
print(quick_select(tab, 0, len(tab)-1, 4))
