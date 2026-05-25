class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            cur = list()
            x = y = i
            while y < n-1-i:
                cur.append(matrix[x][y])
                y += 1
            while x < n-1-i:
                cur.append(matrix[x][y])
                x += 1
            while y > i:
                cur.append(matrix[x][y])
                y -= 1
            while x > i:
                cur.append(matrix[x][y])
                x -= 1
            cur = cur[-(n-1-(2*i)):] + cur[:-(n-1-(2*i))]
            x = y = i
            j = 0
            while y < n-1-i:
                matrix[x][y] = cur[j]
                y += 1
                j += 1
            while x < n-1-i:
                matrix[x][y] = cur[j]
                x += 1
                j += 1
            while y > i:
                matrix[x][y] = cur[j]
                y -= 1
                j += 1
            while x > i:
                matrix[x][y] = cur[j]
                x -= 1
                j += 1


    