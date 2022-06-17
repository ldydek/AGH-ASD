# At the beginning, I receive complete graph (if I consider flights as well). So solution comes to running Dijkstra's
# algorithm. To get O(n^2) time complexity instead of allocating priority queue and putting new vertices in it, I use
# linear searching in a "distance" array to find next graph vertex to consider.
# Time complexity: O(n^2)
# Space complexity: O(n)
# Passed all tests

from kol3btesty import runtests


# O(n)
def choose_vertex(distance, visited):
    index, value = None, float("inf")
    for x in range(len(distance)):
        if distance[x] < value and visited[x] == 0:
            value = distance[x]
            index = x
    return index


# O(1)
def relax1(distance, vertex, x, y):
    if distance[x] > distance[vertex] + y:
        distance[x] = distance[vertex] + y


# O(1)
def relax2(distance, vertex, x, A):
    if distance[x] > distance[vertex] + A[vertex] + A[x]:
        distance[x] = distance[vertex] + A[vertex] + A[x]


# O(n^2)
def airports(G, A, s, t):
    n = len(G)
    distance = [float("inf")] * n
    distance[s] = 0
    visited = [0] * n

    while True:
        vertex = choose_vertex(distance, visited)
        visited[vertex] = 1
        if vertex == t:
            return distance[vertex]
        for x, y in G[vertex]:
            relax1(distance, vertex, x, y)
        for x in range(n):
            relax2(distance, vertex, x, A)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
