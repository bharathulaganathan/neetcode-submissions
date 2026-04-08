class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        def find_word(i, x, y):
            if i >= len(word):
                self.found = True
                return
            if x-1 >= 0:
                if board[x-1][y] == word[i]:
                    find_word(i+1, x-1, y)
            if x+1 < len(board):
                if board[x+1][y] == word[i]:
                    find_word(i+1, x+1, y)
            if y-1 >= 0:
                if board[x][y-1] == word[i]:
                    find_word(i+1, x, y-1)
            if y+1 < len(board[x]):
                if board[x][y+1] == word[i]:
                    find_word(i+1, x, y+1)
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == word[0]:
                    find_word(1, x, y)
        return self.found