# Suppose that first row in a matrix is a green colour, second - red and third one - blue. In each iteration I switch
# colours in a given lamps, so change values from 1 to 0 and from 0 to 1 in appropriate places in a matrix. After each
# iteration I keep information about number of lamps that glow blue and change it if number of them become bigger.
# Time complexity: O(n + T), where "T" is a number of all switchers pushing
# Space complexity: O(3n) = O(n)
# Passed all tests

def find_index(matrix, x):
    for y in range(3):
        if matrix[y][x] == 1:
            return y


def lamps(n, L):
    matrix = [[0 for _ in range(n)] for _ in range(3)]
    for x in range(n):
        matrix[0][x] = 1
    ctr, solution = 0, 0
    for x in range(len(L)):
        for y in range(L[x][0], L[x][1]+1):
            index = find_index(matrix, y)
            matrix[index][y] = 0
            matrix[(index+1) % 3][y] = 1
            if index == 2:
                ctr -= 1
            elif index + 1 == 2:
                ctr += 1
        solution = max(solution, ctr)
    return solution


print(lamps(8, [(0, 4), (2, 6)]))
