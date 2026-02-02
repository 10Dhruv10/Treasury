class unionfind:
    def __init__(self, n):
        self.size = [1]*n
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if self.parent[parent_x] != self.parent[parent_y]:
            if self.size[parent_x] >= self.size[parent_y]:
                self.size[parent_x] += self.size[parent_y]
                self.parent[parent_y] = parent_x
            else:
                self.size[parent_y] += self.size[parent_x]
                self.parent[parent_x] = parent_y

            self.count -= 1

        else:
            return "Cycle"

def helper(n):
    uf = unionfind(n)

