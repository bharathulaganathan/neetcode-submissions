class Trie:
    def __init__(self):
        self.child = dict()
        self.index = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m = len(board)
        self.n = len(board[0])
        self.root = Trie()
        for i, word in enumerate(words):
            cur = self.root
            for w in word:
                if w not in cur.child:
                    cur.child[w] = Trie()
                cur = cur.child[w]
            cur.index = i
        self.res = list()
        def checkwords(cur, x, y, done):
            if cur.index >= 0:
                self.res.append(words[cur.index])
                cur.index = -1
            s = board[x][y]
            done.add((x,y))
            if s in cur.child:
                cur = cur.child[s]
                for i, j in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nx = x+i
                    ny = y+j
                    if (nx,ny) not in done:
                        new_done = done.copy()
                        if nx >= 0 and nx < self.m and ny >= 0 and ny < self.n:
                            checkwords(cur, nx, ny, new_done)
        for i in range(len(board)):
            for j in range(len(board[i])):
                checkwords(self.root, i, j, set())
        return self.res