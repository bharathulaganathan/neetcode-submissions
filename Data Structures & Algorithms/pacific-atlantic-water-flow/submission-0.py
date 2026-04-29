class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        drain = set()
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            for j in range(n):
                crossed = set()
                q = deque()
                q.append((i,j))
                pac = False
                atl = False
                while q:
                    cur = q.popleft()
                    if cur in drain:
                        pac = True
                        atl = True
                        break
                    crossed.add(cur)
                    ni, nj = cur
                    for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                        ix = ni+x
                        jy = nj+y
                        if ix >= 0 and ix < m and jy >= 0 and jy < n and (ix,jy) not in crossed and heights[ix][jy] <= heights[ni][nj]:
                            q.append((ix,jy))
                    if ni == 0 or nj == 0:
                        pac = True
                    if ni == m-1 or nj == n-1:
                        atl = True
                    if pac == True and atl == True:
                        break
                if pac == True and atl == True:
                    drain.add((i,j))
        return [list(h) for h in drain]
