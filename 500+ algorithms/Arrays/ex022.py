# Contiguous subarray with the largest sum.

def ex022(tab):
    n = len(tab)
    sum, answer = 0, 0
    for x in range(n):
        sum += tab[x]
        if sum < 0:
            sum = 0
        answer = max(answer, sum)
    return answer


tab = [-2, 1, -3, 4, 1, 2, 1, -5, 4]
print(ex022(tab))
