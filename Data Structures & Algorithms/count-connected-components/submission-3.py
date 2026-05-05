class Union:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.root = [0] * n
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def join(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.root[root_x] > self.root[root_y]:
            self.parent[y] =  x
        elif self.root[root_y] > self.root[root_x]:
            self.parent[x] =  y
        else:
            self.parent[y] = x
            self.root[x] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union = Union(n)
        for x,y in edges:
            union.join(x,y)
        res = set()
        for i in range(n):
            union.find(i)
            res.add(union.parent[i])
        return len(res)