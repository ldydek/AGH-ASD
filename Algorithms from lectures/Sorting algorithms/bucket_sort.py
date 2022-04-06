# [ENG] In bucket sort algorithm we create 2D array and each row is an empty list at the beginning and it's called
# a bucket. To that lists we will be appending certain data. Assuming that in each row there are several elements we
# can sort that elements, for instance, insertion sort algorithm. As for each element in a certain bucket each
# element from another bucket is less or greater than this one we can, at the end, merge all that buckets and get
# the sorted array. If we have "n" elements to sort, good idea is to create "n" buckets. Algorithm can work in linear
# time only if data is generated from uniform distribution!
# Time complexity: θ(n) if we assume that data is generated from uniform distribution.
# [PL] Algorytm sortowania kubełkowego polega na podzieleniu danych do posortowania tak, aby mniej więcej tyle samo
# trafiło do jednego kubełka. Kubełkiem natomiast może być zwykła tablica zawierająca średnio kilka elementów.
# Sortujemy dane w każdym kubełku algorytmem sortowania przez wstawianie. Na końcu, łącząc kubełki, otrzymujemy
# posortowany ciąg danych. Jeżeli do posortowania mamy "n" liczb, to dobrym pomysłem będzie utworzenie "n" rozłącznych
# podprzedziałów tzw. kubełków. Dane do posortowania muszą jednak spełniać jeden podstawowy warunek: musimy mieć
# pewność, że pochodzą z rozkładu jednostajnego dzięki czemu w każdym kubełku będzie ich niewiele a konkretniej zbliżona
# do siebie ilość.
# Złożoność czasowa: θ(n) przy założeniu, że dane pochodzą z rozkładu jednostajnego.

def bucket_sort(tab):
    n = len(tab)
    buckets = [[] for _ in range(n+1)]
    mini = min(tab)
    maxi = max(tab)
    interval = (maxi - mini) // n
    for x in range(n):
        buckets[int((tab[x]-mini)//interval)].append(tab[x])
    for x in range(n):
        insertion_sort(buckets[x])
    ctr = 0
    for x in range(n):
        for y in range(len(buckets[x])):
            tab[ctr] = buckets[x][y]
            ctr += 1
    return tab


def insertion_sort(tab):
    n = len(tab)
    for x in range(1, n):
        key = tab[x]
        y = x - 1
        while y >= 0 and tab[y] > key:
            tab[y+1] = tab[y]
            y = y - 1
        tab[y+1] = key
    return tab


tab = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68, 99, 95, 97, 99]
print(bucket_sort(tab))
