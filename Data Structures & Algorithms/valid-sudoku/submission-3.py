class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(list), defaultdict(list), defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                squares[(r//3,c//3)].append(board[r][c])
        
        return True
