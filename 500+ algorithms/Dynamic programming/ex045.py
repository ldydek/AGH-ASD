# Time complexity: O(mn)
# Space complexity: O(k^2)

def ex045(matrix, k):
    m, n = len(matrix), len(matrix[0])
    for x in range(1, m):
        matrix[x][0] += matrix[x-1][0]
    for x in range(1, n):
        matrix[0][x] += matrix[0][x-1]
    for x in range(1, m):
        for y in range(1, n):
            matrix[x][y] += matrix[x-1][y] + matrix[x][y-1] - matrix[x-1][y-1]
    a1, b1 = k-1, k-1
    s1, s2 = None, None
    final_value = -10**10
    for x in range(a1, m):
        for y in range(b1, n):
            if x >= k and y >= k:
                value = matrix[x][y] - matrix[x-k][y] - matrix[x][y-k] + matrix[x-k][y-k]
            elif x >= k:
                value = matrix[x][y] - matrix[x-k][y]
            elif y >= k:
                value = matrix[x][y] - matrix[x][y-k]
            else:
                value = matrix[x][y]
            if value > final_value:
                final_value = value
                s1, s2 = x, y
    return print_solution(matrix, s1-k+1, s2-k+1, k)


def element(tab, x, y):
    if x > 0 and y > 0:
        return tab[x][y] - tab[x-1][y] - tab[x][y-1] + tab[x-1][y-1]
    elif x > 0:
        return tab[x][y] - tab[x-1][y]
    elif y > 0:
        return tab[x][y] - tab[x][y-1]


def print_solution(tab, a, b, k):
    solution = [[None for _ in range(k)] for _ in range(k)]
    for x in range(k):
        for y in range(k):
            solution[x][y] = element(tab, a+x, b+y)
    return solution


matrix = [
        [3, -4, 6, -5, 1],
        [1, -2, 8, -4, -2],
        [3, -8, 9, 3, 1],
        [-7, 3, 4, 2, 7],
        [-3, 7, -5, 7, -6]]
print(ex045(matrix, 3))
