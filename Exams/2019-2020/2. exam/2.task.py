# Idea is to run Kruskal's algorithm on the entire edge list. Then we receive minimum spanning tree. Later, we consider
# again previous edge list but this time without first element. Again we receive spanning tree after find-union method
# but this time not minimum. Each time we get the tree we write down weights between heaviest and lightest edge in it.
# Time complexity: O(E log V + E^2) = O(E^2) = O(V^4)
# Space complexity: O(V)
# Passed all tests


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


A = [(100, 100), (100, 200), (200, 100), (200, 200), (150, 151)]
print(highway(A))
