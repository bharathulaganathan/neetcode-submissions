class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for _ in range(n)] for _ in range(m)]
        res[0][0] = 1
        q = deque()
        q.append((0,0))
        done = set()
        while q:
            i, j = q.popleft()
            cur = res[i][j]
            for x, y in [(0,1), (1,0)]:
                if i+x < m and j+y < n:
                    res[i+x][j+y] += cur
                    if (i+x,j+y) not in done:
                        q.append((i+x,j+y))
                        done.add((i+x,j+y))
        return res[m-1][n-1]