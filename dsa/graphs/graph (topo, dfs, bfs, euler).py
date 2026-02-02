from collections import *

class Solution:
    def kahns(self, numCourses, prerequisites):

        neighbours = defaultdict(list)
        indegree = [0] * numCourses
        for src, dest in prerequisites:
            neighbours[src].append(dest)
            indegree[dest] += 1

        q = deque([i for i in range(len(indegree)) if indegree[i] == 0])
        res = []

        while q:
            cur = q.popleft()
            res.append(cur)

            for neighbor in neighbours[cur]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return len(res) == numCourses

#WorstCase time & space: O(V²)

