class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        def find_word(i, x, y, done):
            if i >= len(word):
                self.found = True
                return
            if self.found:
                return
            if x-1 >= 0 and board[x-1][y] == word[i] and (x-1,y) not in done:
                    new_done = done.copy()
                    new_done.add((x-1,y))
                    find_word(i+1, x-1, y, new_done)
            if x+1 < len(board) and board[x+1][y] == word[i] and (x+1,y) not in done:
                    new_done = done.copy()
                    new_done.add((x+1,y))
                    find_word(i+1, x+1, y, new_done)
            if y-1 >= 0 and board[x][y-1] == word[i] and (x,y-1) not in done:
                    new_done = done.copy()
                    new_done.add((x,y-1))
                    find_word(i+1, x, y-1, new_done)
            if y+1 < len(board[x]) and board[x][y+1] == word[i] and (x,y+1) not in done:
                    new_done = done.copy()
                    new_done.add((x,y+1))
                    find_word(i+1, x, y+1, new_done)
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == word[0]:
                    find_word(1, x, y, set([(x,y)]))
        return self.found