from collections import *

def isBipartite(graph):
    adj = defaultdict(list)
    n = len(graph)
    for i in range(n):
        adj[i].extend(graph[i])

    colors = [-1] * n

    for node in range(n):

        if colors[node] != -1:
            continue

        q = deque([node])
        colors[node] = 0

        while q:
            cur = q.popleft()

            for nei in adj[cur]:
                neiColor = colors[nei]

                if neiColor == -1:
                    colors[nei] = 1 - colors[cur]
                    q.append(nei)

                if neiColor == colors[cur]:
                    return False

    return True

'''
Bipartite is a graph which can be divided into 2 sets
where all the edges existing in graph has one edge 
in set A and other in set B, both sets can have nodes
with no edged at all as well

A complete bipartite graph has each node in setA
connecting with a node in set B

To find if a graph is bipartite, we color its node 
with 0 or 1, if a parent is 0 then neighbours are 1, 
and vice versa, if we end up having 0-0 or 1-1 being 
parent and neighbour then it's not bipartite which 
happens in odd length cycle graph

All non-cyclic graph are bipartite

'''

'''
we can have multiple connected components like 
0-1-2-3-0 and 4-5-6-4 in question

we will need to run a for loop for this, as to catch the 
beginning of each components in our queue

for graph to be bipartite:-
    mark a node with 0 and its neighbours with 1
            or viceversa

    in brief 2 adjacent nodes must be either 0-1 or 1-0
    and if they are 0-0 or 1-1 that means graph is not bipartite
    (odd length cycles are not bipartite)
'''