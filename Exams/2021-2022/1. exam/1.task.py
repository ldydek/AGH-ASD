# Idea is to sort given list decreasingly and greedily choose the biggest available snow areas. After each day we
# subtract from snow area certain number (how much snow was melted) and add given amount to the final solution. We
# are forced to repeat that until we traverse entire list or amount of next snow area will be 0 (whole snow was melted).
# Time complexity: O(n log n) - sorting
# Space complexity: O(1)
# Passed all tests
# Time for all tests: ~ 0.5s

from egz1atesty import runtests


def snow(S):
    S.sort(reverse=True)
    snow_quantity, ctr, index = 0, 0, 0
    while index < len(S) and S[index] >= ctr:
        snow_quantity += (S[index] - ctr)
        index += 1
        ctr += 1
    return snow_quantity


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
