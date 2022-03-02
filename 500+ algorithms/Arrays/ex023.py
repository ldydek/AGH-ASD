def ex023(tab):
    n = len(tab)
    sum, answer = 0, 0
    index = None
    solution = []
    for x in range(n):
        sum += tab[x]
        if sum < 0:
            sum = 0
        if answer < sum:
            answer = sum
            index = x
    sum = 0
    while sum < answer:
        sum += tab[index]
        solution.append(tab[index])
        index -= 1
    return solution[::-1]


tab = [-2, 1, -3, -4, 1, -2, 1, 5, 4]
print(ex023(tab))
