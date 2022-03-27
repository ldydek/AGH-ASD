# O(n)
def ex06(tab):
    n = len(tab)
    mini, maxi = 10**10, -10**10
    for x in range(n):
        mini = min(mini, tab[x])
        maxi = max(maxi, tab[x])
    i = (maxi - mini) / n
    buckets = [[] for _ in range(n+1)]
    for x in range(n):
        buckets[int((tab[x]-mini)//i)].append(tab[x])
    x, range1 = 0, 0
    a, b = None, None
    while len(buckets[x]) == 0:
        x += 1
    maxi = max(buckets[x])
    while x < n:
        if len(buckets[x]):
            mini = min(buckets[x])
            if mini - maxi > range1:
                range1 = mini - maxi
                a, b = maxi, mini
            maxi = max(buckets[x])
        x += 1
    return a, b


tab = [11, 9, 1, 17, 47, 32, 36, 51, 42, 58, 26, 20]
print(ex06(tab))
