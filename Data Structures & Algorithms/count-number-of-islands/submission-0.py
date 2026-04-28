class Union:
    def __init__(self,m,n):
        self.parent = [i for i in range(m*n)]
        self.rank = [0 for _ in range(m*n)]
    
    def find(self,v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def join(self,r,l):
        root_r = self.find(r)
        root_l = self.find(l)
        if root_r == root_l:
            return
        if self.rank[r] > self.rank[l]:
            self.parent[root_l] = root_r
        elif self.rank[l] > self.rank[r]:
            self.parent[root_r] = root_l
        else:
            self.parent[root_l] = root_r
            self.rank[r] += 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        union = Union(m,n)
        done = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if i+1 < m and grid[i+1][j] == "1":
                        union.join((i*n+j),((i+1)*n+j))
                    if j+1 < n and grid[i][j+1] == "1":
                        union.join((i*n+j),(i*n+(j+1)))
                else:
                    union.parent[i*n+j] = -1
        for i in range(m):
            for j in range(n):
                union.find(i*n+j)
        res = set(union.parent)
        if -1 in res:
            res.remove(-1)
        return len(res)
