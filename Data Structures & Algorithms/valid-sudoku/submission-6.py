class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rl, cl = len(board), len(board[0])
        cols, rows, sqrs = defaultdict(list), defaultdict(list), defaultdict(list)
        for r in range(rl):
            for c in range(cl):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqrs[(r//3,c//3)]:
                    return False
                cols[c].append(board[r][c])
                rows[r].append(board[r][c])
                sqrs[(r//3,c//3)].append(board[r][c])
        return True


