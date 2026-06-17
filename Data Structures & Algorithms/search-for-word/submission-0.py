class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
    
        def dfs(r, c, index):
            # Base cases
            if index == len(word):  # All characters matched
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all 4 directions
            res = (dfs(r + 1, c, index + 1) or  # Down
                dfs(r - 1, c, index + 1) or  # Up
                dfs(r, c + 1, index + 1) or  # Right
                dfs(r, c - 1, index + 1))    # Left

            # Restore the cell value (backtracking)
            board[r][c] = temp
            return res

        # Start from each cell in the grid
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # Optimization: Only start DFS if the first letter matches
                    if dfs(i, j, 0):
                        return True

        return False