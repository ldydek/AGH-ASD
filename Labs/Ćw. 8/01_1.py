# Checking if a graph is bipartite using BFS. I traverse the graph and start classifying vertices to two sets. During
# considering a certain vertex there are two cases: either its neighbour is not visited and we can mark this vertex
# as a part of a second set or it was already visited and it has to be already a part of a second set. If certain vertex
# and one of its neighbours have the same number that classifies them to the same set it means that this graph is not
# bipartite. If this situation won't happen graph is bipartite. Additionally I suppose here that given graph don't have
# to be consistent.

from collections import deque


def bfs(graph, distance, x, queue):
    queue.append(x)
    distance[x] = 0
    while queue:
        u = queue.popleft()
        for x in range(len(graph[u])):
            if distance[graph[u][x]] is None:
                distance[graph[u][x]] = (distance[u] + 1) % 2
                queue.append(graph[u][x])
            elif distance[graph[u][x]] == distance[u]:
                return False


def ex01(graph):
    queue = deque()
    n = len(graph)
    distance = [None] * n
    for x in range(len(graph)):
        if distance[x] is None:
            if bfs(graph, distance, x, queue) is False:
                return False
    return True


graph = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1, 5], [4, 7], [7], [5, 6], [9], [8]]
print(ex01(graph))
