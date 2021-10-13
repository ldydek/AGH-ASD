# Sortowanie kubełkowe polega na podzieleniu danych do posortowania tak, aby mniej więcej tyle samo trafiło do jednego
# kubełka. Kubełkiem natomiast może być zwykła tablica zawierająca średnio kilka elementów. Sortujemy dane
# w każdym kubełku algorytmem sortowania przez wstawianie. Na końcu łącząc kubełki otrzymujemy posortowany ciąg danych.
# Jeżeli do posortowania mamy n liczb, to dobrym pomysłem będzie utworzenie n rozłącznych podprzedziałów tzw. kubełków.
# Dane do posortowania muszą jednak spełniać jeden podstawowy warunek: musimy mieć pewność, że pochodzą z rozkładu
# jednostajnego dzięki czemu w każdym kubełku będzie ich niewiele a konkretniej zbliżona do siebie ilość.
# Złożoność czasowa: O(n)

def bucket_sort(tab):
    n = len(tab)
    buckets = [[] for x in range(10)]
    for x in range(n):
        buckets[tab[x]//10].append(tab[x])
    for x in range(10):
        for y in range(1, len(buckets[x])):
            key = buckets[x][y]
            z = y - 1
            while z >= 0 and buckets[x][z] > key:
                buckets[x][z + 1] = buckets[x][z]
                z = z - 1
            buckets[x][z + 1] = key
    ctr = 0
    for x in range(10):
        for y in range(len(buckets[x])):
            tab[ctr] = buckets[x][y]
            ctr += 1
    return tab


tab = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68, 99, 95, 97, 99]
print(bucket_sort(tab))
