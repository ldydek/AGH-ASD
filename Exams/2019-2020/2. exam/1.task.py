# Frog can eat unlimited amount of food, so we can use here greedy approach. I allocate priority queue and at each time
# I get from it a field with the biggest possible temporary energy. This structure is necessary here, because this place
# can be either before or after previous considered field. At each time, I choose best field counter is increased,
# because on that field frog will stop. If frog will have sufficient amount of energy to jump to the last field, we can
# just return a solution.
# Time complexity: O(n log n)
# Space complexity: O(n log n)
# Passed all tests

from queue import PriorityQueue


def zbigniew(A):
    n = len(A)
    queue = PriorityQueue()
    solution = 0
    queue.put((-A[0], 0))
    while not queue.empty():
        a, b = queue.get()
        a = -a
        solution += 1
        energy = a
        for x in range(b+1, min(b+a+1, n)):
            energy -= 1
            if A[x] > 0:
                queue.put((-energy-A[x], x))
                if energy + A[x] + x >= n-1:
                    solution += 1
                    return solution
    return -1


A = [2, 2, 1, 0, 0, 0]
print(zbigniew(A))


------------------------------------------------------------------------------------
# Dynamic programming approach
# f(i, j) - minimum number of jumps to get to A[i] having "j" energy after consuming
# energy level before eating - max(0, j-A[i])
# recursion: f(i, j) = min(f(i-k, max(0, j-A[i])+k), where 1 <= k <= i
# basic cases: f(0, min(A[0], n-1)) = 0, where "n" is the array length
# Time complexity: O(n^3)
# Space complexity: O(n^2)
# Passed all tests

from zad1testy import runtests


def zbigniew( A ):
    n = len(A)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]
    # basic cases
    for x in range(min(n, A[0]+1)):
        dp[0][x] = 1

    # pure dynamic programming
    for x in range(1, n):
        for y in range(n):
            value = float("inf")
            for k in range(1, x+1):
                before_eat = max(0, y - A[x])
                value = min(value, dp[x-k][before_eat + k])
            dp[x][y] = value + 1
            # condition happens when jumping to "x" field with "y" energy after consuming is possible
            # and additionally energy level allows Zbigniew to jump to the last field
            if dp[x][y] != float("inf") and y >= n - x - 1:
                return dp[x][y]
       

runtests(zbigniew)
