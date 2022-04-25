# Firstly, we have to do small preprocessing of a matrix. During traversing first row if we meet positive field with
# a fuel we count value of entire stain and keep it in one field in the first row (the same which was positive at the
# beginning and we meet it). Now I can greedily after first fuelling choose next field in a range of fuel with the
# biggest number. After second fuelling range widens and again I choose a field with the biggest number. To do it, we
# have to allocate priority queue, because next optimal fields can be either before considering field or after. All the
# time when I choose optimal place I add it to the solution.
# Time complexity: O(nm)
# Space complexity: O(nm) - we can pick stain from the entire board
# Passed all tests

from queue import PriorityQueue


def take_fuel(T, row, column, fuel):
    n = len(T[0])
    fuel[0] += T[row][column]
    T[row][column] = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for x in range(len(directions)):
        if 0 <= column + directions[x][1] <= n-1 and 0 <= row + directions[x][0] <= n-1:
            if T[row+directions[x][0]][column + directions[x][1]] > 0:
                fuel[0] += T[row+directions[x][0]][column + directions[x][1]]
                T[row+directions[x][0]][column + directions[x][1]] = 0
                take_fuel(T, row + directions[x][0], column + directions[x][1], fuel)


def plan(T):
    m = len(T[0])
    fuel = [0]
    stops = []
    for x in range(m):
        if T[0][x] > 0:
            take_fuel(T, 0, x, fuel)
            T[0][x] = fuel[0]
            fuel[0] = 0
    queue = PriorityQueue()
    total_fuel = 0
    for i in range(m - 1):
        if T[0][i] != 0:
            queue.put((-T[0][i], i))
        if total_fuel == 0:
            actual_value = queue.get()
            total_fuel -= actual_value[0]
            stops.append(actual_value[1])
        total_fuel -= 1
    stops.sort()
    return stops


T = [[5, 0, 1, 0, 0, 2, 0],
 [0, 1, 0, 0, 0, 1, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0]]
print(plan(T))
