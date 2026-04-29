class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pac = set()
        atl = set()
        for i in range(m):
            pac.add((i,0))
            atl.add((i,n-1))
        for j in range(n):
            pac.add((0,j))
            atl.add((m-1,j))
        for i in range(1,m):
            for j in range(1,n):
                cur = heights[i][j]
                if ((i-1,j) in pac and heights[i-1][j] <= cur) or ((i,j-1) in pac and heights[i][j-1] <= cur):
                    pac.add((i,j))
                ni = m-i-1
                nj = n-j-1
                cur = heights[ni][nj]
                if ((ni+1,nj) in atl and heights[ni+1][nj] <= cur) or ((ni,nj+1) in atl and heights[ni][nj+1] <= cur):
                    atl.add((ni,nj))
        res = pac & atl
        return [list(x) for x in res]