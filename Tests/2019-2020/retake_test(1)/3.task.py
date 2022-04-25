# Idea is to allocate additional array and keep data how many individual elements are in considering subsequence, for
# instance, 5 is once, 2 is twice etc in the subsequence (a,..,x). If all "k" numbers is present I move second pointer
# from the beginning of the array decreasing occurrence of the element in auxiliary array. This situation has to be
# repeated until occurrence of certain element will be 0. If, so I can move front pointer further.
# Time complexity: O(nk) = O(n), because k <<< n
# Space complexity: O(k)
# Passed all tests

from math import inf


# function which helps us increase occurrence of given element in a subsequence
def increase_element(numbers, k, ctr):
    for x in range(len(numbers)):
        if numbers[x][0] == k:
            if numbers[x][1] == 0:
                ctr += 1
            numbers[x] = (numbers[x][0], numbers[x][1]+1)
            return ctr


# the same like above but this time decreasing
def decrease_element(numbers, k, ctr):
    for x in range(len(numbers)):
        if numbers[x][0] == k:
            numbers[x] = (numbers[x][0], numbers[x][1]-1)
            if numbers[x][1] == 0:
                ctr -= 1
            return ctr


# ctr - variable holding information how many distinct numbers are in the subsequence
# numbers - auxiliary array with tuples: (number, its occurrence)
def longest_incomplete(A, k):
    n = len(A)
    numbers = []
    solution = -inf
    a, ctr = 0, 0
    for x in range(n):
        if A[x] not in numbers:
            numbers.append(A[x])
    for x in range(k):
        numbers[x] = (numbers[x], 0)
    for x in range(n):
        while ctr == k:
            ctr = decrease_element(numbers, A[a], ctr)
            a += 1
        else:
            ctr = increase_element(numbers, A[x], ctr)
            if ctr != k:
                solution = max(solution, x-a+1)
    return solution


A = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(longest_incomplete(A, 3))
