class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        done = set()
        move = (0,1)
        change = {(0,1): (1,0), (1,0): (0,-1), (0,-1): (-1,0), (-1,0): (0,1)}
        res = list()
        nxt = (0,0)
        while nxt not in done:
            done.add(nxt)
            x,y = nxt
            res.append(matrix[x][y])
            i,j = move
            nx = x+i
            ny = y+j
            if (nx,ny) in done or nx >= m or nx < 0 or ny >= n or ny < 0:
                move = change[move]
                i,j = move
                nxt = (x+i, y+j)
            else:
                nxt = (nx,ny)
        return res



        