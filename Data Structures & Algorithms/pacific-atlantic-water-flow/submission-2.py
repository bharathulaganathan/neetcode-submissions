class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pac = set()
        atl = set()
        for ocn, sx, sy in [[pac,0,0], [atl,m-1,n-1]]:
            q = deque()
            for i in range(m):
                q.append((i,sy))
            for j in range(n):
                q.append((sx,j))
            while q:
                cur = q.popleft()
                ocn.add(cur)
                i,j = cur
                val = heights[i][j]
                for x,y in [[0,1],[0,-1],[1,0],[-1,0]]:
                    ni = i+x
                    nj = j+y
                    if ni >= 0 and ni < m and nj >= 0 and nj < n and (ni,nj) not in ocn and heights[ni][nj] >= val:
                        q.append((ni,nj))
        res = pac & atl
        return [list(x) for x in res]