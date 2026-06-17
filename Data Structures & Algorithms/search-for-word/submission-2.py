class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True    
            if r >= row_len or r < 0 or c >= col_len or c < 0 or board[r][c] != word[i] or board[r][c] == '#':
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'
            res = (dfs(i+1, r + 1, c) or
                  dfs(i+1, r - 1, c) or 
                  dfs(i+1, r, c + 1) or
                  dfs(i+1, r, c - 1))
            board[r][c] = tmp

            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True

        return False