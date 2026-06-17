class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares_map = defaultdict(list)
        rows_map = defaultdict(list)
        cols_map = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows_map[r] or board[r][c] in cols_map[c] or board[r][c] in squares_map[(r//3,c//3)]:
                    return False
                else:
                    squares_map[(r//3,c//3)].append(board[r][c])
                    rows_map[r].append(board[r][c])
                    cols_map[c].append(board[r][c])
        return True