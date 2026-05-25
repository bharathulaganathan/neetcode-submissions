class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        rows = list(rows)
        for r in rows:
            for j in range(n):
                matrix[r][j] = 0
        cols = list(cols)
        for i in range(m):
            for c in cols:
                matrix[i][c] = 0