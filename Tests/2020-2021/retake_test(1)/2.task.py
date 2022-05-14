# Small modification of finding articulation points algorithm. This time we don't need to print all of them but only
# one specified. How to find it? When we look at DFS tree this articulation point (let's call it "v") which has the most
# number of subtrees rooted in its children without back edges to one of "v" ancestor is this one we search. So during
# DFS traversal when we visit one subtree without back edge to "v" ancestor we just increment number of this counted
# subtrees and write new value down in an auxiliary array for "v" vertex. At the end, we check if graph has any
# articulation points and if so, we choose this one with the greatest value in this auxiliary array. Obviously, we omit
# DFS tree root and, at the end, we compare chosen value with number of root children.
# Time complexity: O(V + E) - dfs algorithm
# Space complexity: O(V)
# Passed all tests

from zad2testy import runtests
from math import inf


def dfs(graph, distance, low, parent, time_and_children, if_point, x):
    time_and_children[0] += 1
    distance[x] = time_and_children[0]
    low[x] = time_and_children[0]
    for i in range(len(graph[x])):
        if graph[x][i] == 0:
            continue
        if distance[i] == inf:
            if time_and_children[2] == x:
                time_and_children[1] += 1
            parent[i] = x
            low[x] = min(low[x], dfs(graph, distance, low, parent, time_and_children, if_point, i))
            if low[i] >= distance[x]:
                if_point[x] += 1
        elif parent[x] != i:
            low[x] = min(low[x], distance[i])
    return low[x]


def breaking(graph):
    n = len(graph)
    distance = [inf] * n
    low = [inf] * n
    parent = [-1] * n
    root = 0
    time_and_children = [0, 0, root]
    # array with data: distance time (dfs traversal), number of root children, root
    if_point = [0] * n
    # if_point array later will hold data:
    # 0 - no articulation point
    # x > 0 - articulation point with "x" subtrees without back edge
    dfs(graph, distance, low, parent, time_and_children, if_point, root)
    index = 1
    # searching for an appropriate articulation point if it exists
    for x in range(1, n):
        if if_point[x] > if_point[index]:
            index = x
    if time_and_children[1] == 1 and if_point[index] == 0:
        return None
    if time_and_children[1] > if_point[index]:
        return root
    return index


# runtests(breaking)
G = [[0, 1, 1, 0, 0],
[1, 0, 1, 0, 0],
[1, 1, 0, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0]]
print(breaking(G))
