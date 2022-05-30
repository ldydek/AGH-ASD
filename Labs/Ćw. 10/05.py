# |E| times I determine spanning tree on this graph using find-union technique. First time it will be MST. Later, I 
# consider sublist of edge list apart from "n" first elements, so I will get certain spanning tree but not MST.
# Each time I additionally compute difference between the heaviest and lightest edge weight in a spanning tree.
# Time complexity: O(E log V + E^2) = O(E^2)
# Space complexity: O(E)

def kruskal_algorithm(tab, p, r, n):
    included = [0] * n
    parent = [x for x in range(n)]
    rank = [0 for _ in range(n)]
    for x in range(p, r):
        included[tab[x][0]] = 1
        included[tab[x][1]] = 1
    for x in range(len(parent)):
        if included[x] == 0:
            return float("inf")
    min_value = float("inf")
    max_value = float("-inf")
    ctr = 0
    for x in range(p, r):
        if find(parent, tab[x][0]) != find(parent, tab[x][1]):
            union(tab[x][0], tab[x][1], parent, rank)
            ctr += 1
            min_value = min(min_value, tab[x][2])
            max_value = max(max_value, tab[x][2])
            if ctr == n - 1:
                return max_value - min_value


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(x, y, parent, rank):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1


def length(x, y):
    dist = ((x[0]-y[0])**2 + (x[1]-y[1])**2) ** (1/2)
    if int(dist) == dist:
        return int(dist)
    return int(dist) + 1


def highway(A):
    n = len(A)
    if n == 1:
        return 0
    edges = []
    for x in range(n):
        for y in range(x+1, n):
            edges.append((x, y, length(A[x], A[y])))
    edges.sort(key=lambda x: x[2])
    solution = float("inf")
    for x in range(len(edges)-n+2):
        solution = min(solution, kruskal_algorithm(edges, x, len(edges), n))
    return solution


A = [(10, 10), (15, 25), (20, 20), (30, 40)]
print(highway(A))
