#djikstra

#directed, undirected
from collections import *
import heapq

def djikstra(times, n, source) -> int:
    graph, hq, src = defaultdict(list), [], source

    for u, v, w in times:
        graph[u].append((v, w))

    heapq.heappush(hq, (0, src))
    shortest = {}

    while hq:
        w, v = heapq.heappop(hq)

        if v in shortest: continue
        shortest[v] = w

        for (v2, w2) in graph[v]:
            if v2 not in shortest:
                heapq.heappush(hq, (w+w2, v2))

    return max(shortest.values()) if len(shortest)==n else -1



#kruskal

class unionfind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.size[parent_x] >= self.size[parent_y]:
                self.parent[parent_y] = parent_x
                self.size[parent_x] += self.size[parent_y]

            else:
                self.parent[parent_x] = parent_y
                self.size[parent_y] += self.size[parent_x]

            return True
        else:
            return False

def kruskal(points):
    n = len(points)
    uf, graph = unionfind(n), []

    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            cost = abs(x1-x2) + abs(y1-y2)

            graph.append((cost, i, j))

    graph.sort()


    res = 0
    for (w, i, j) in graph:
        if uf.union(i, j):
            res += w

    return res

def prim(points):

    hq, n, visited = [], len(points), set()
    size, res = 0, 0
    heapq.heappush(hq, (0, 0))    #2nd 0 is index of beginning point

    while hq:
        w, v = heapq.heappop()

        if v in visited:
            continue

        visited.add(v)
        size += 1
        res += w

        if size == n:
            break

        for (w2, v2) in range(n):
            if v2 not in visited:
                heapq.heappush(hq, (w2, v2))

    return res