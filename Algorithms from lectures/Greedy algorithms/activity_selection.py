# Greedy approach
# At the beginning, I sort activities increasingly with ending time. Later, I greedily choose this activity, which
# starting time is greater or equal to ending time of the previous one. First activity is always included.
# Time complexity: O(n log n)
# Space complexity: additional array that keeps solution - could be O(n)


def activity_selection(tab):
    n = len(tab)
    tab.sort(key=lambda x: x[1])
    solution = [tab[0]]
    end = tab[0][1]
    for x in range(1, n):
        if end <= tab[x][0]:
            solution.append(tab[x])
            end = tab[x][1]
    return solution


tab = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
print(activity_selection(tab))
