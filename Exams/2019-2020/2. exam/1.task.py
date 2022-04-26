# Frog can eat unlimited amount of food, so we can use here greedy approach. I allocate priority queue and at each time
# I get from it a field with the biggest possible temporary energy. This structure is necessary here, because this place
# can be either before or after previous considered field. At each time, I choose best field counter is increased,
# because on that field frog will stop. If frog will have sufficient amount of energy to jump to the last field, we can
# just return a solution.
# Time complexity: O(n log n)
# Space complexity: O(n log n)

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
