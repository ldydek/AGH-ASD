# [ENG] Articulation point is a vertex in a graph whose deletion will cause graph disconnection. To find that points
# we run DFS algorithm, which shows us DFS forest. Now we have certain vertex, let's called it "v". We have to check
# if from one of "v" descendants there is an edge to one of "v" ancestors. If so, this point is not an articulation
# point, because another path between this two parts of a graph still exists. So this vertex will be articulation point
# if from one of this vertex children and for each of this child descendants there is no edge to the "v" ancestor.
# If vertex is a root, it doesn't have a parent, so for that case we have to check whether root has at least two
# children. If so, it is an articulation point, because another part of graph is available only through the root.
# So here is set of steps:
# 1) Run DFS and write down visited time of each vertex
# 2) For each vertex compute low(v):
# low(v) = min(d(v), min(d(u)), min(low(w))), where (v, u) is back edge in a graph and "w" is one of "v" children
# Note that we at first omit information about back edges in a code. We only check how situation looks like in subtrees
# rooted in vertex children. Then we update low also about possible back edges.
# If low(v) >= visited(v), "v" is an articulation point before updating about back edges.
# [PL] Punkt artykulacji to wierzchołek grafu, którego usunięcie spowoduje zwiększenie ilości spójnych składowych.
# Aby takie punkty znaleźć, uruchamiamy DFS, dzięki czemu dostaniemy las przeszukiwania wgłąb. Teraz mamy pewien
# wierzchołek, nazwijmy go sobie "v". Musimy sprawdzić, czy od jednego z potomków "v" w drzewie DFS nie ma krawędzi
# wstecznej do pewnego przodka "v". Jeśli tak jest, to ten wierzchołek nie jest punktem artykulacji, ponieważ istnieje
# inna ścieżka pomiędzy tymi częściami grafu. A więc wierzchołek będzie punktem artykulacji, gdy dla pewnego dziecka
# danego wierzchołka ani od niego, ani od żadnego jego potomka nie będzie krawędzi wstecznej do przodka "v". Jeśli
# "v" jest korzeniem, to gdy ma przynajmniej dwoje dzieci, to także jest punktem artykulacji, ponieważ aby dostać
# się do drugiego poddrzewa jesteśmy zmuszeni ponownie przez korzeń przejść.
# Lista kroków powyżej po angielsku.
from math import inf


def dfs(graph, distance, low, parent, time_and_children, if_point, x):
    time_and_children[0] += 1
    distance[x] = time_and_children[0]
    low[x] = time_and_children[0]
    for v in graph[x]:
        if distance[v] == inf:
            if time_and_children[2] == x:
                time_and_children[1] += 1
            parent[v] = x
            low[x] = min(low[x], dfs(graph, distance, low, parent, time_and_children, if_point, v))
            if low[v] >= distance[x]:
                if_point[x] = 1
        elif parent[x] != v:
            low[x] = min(low[x], distance[v])
    return low[x]


def articulation_points(graph):
    n = len(graph)
    distance = [inf] * n
    low = [inf] * n
    parent = [-1] * n
    time_and_children = [0, 0, 0]
    if_point = [0] * n
    solution = []
    root = 0
    dfs(graph, distance, low, parent, time_and_children, if_point, root)
    if time_and_children[1] >= 2:
        solution.append(0)
    for x in range(n):
        if x == root:
            continue
        if if_point[x] == 1:
            solution.append(x)
    return solution


graph = [[1, 4], [0, 2], [1, 3, 4], [2], [0, 2, 5], [4, 6, 7], [5, 7], [5, 6]]
print(articulation_points(graph))
