class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map, col_map, sqre_map = defaultdict(list), defaultdict(list), defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue

                if board[r][c] in row_map[r] or board[r][c] in col_map[c] or board[r][c] in sqre_map[(r//3,c//3)]:
                    return False 
                
                row_map[r].append(board[r][c]) 
                col_map[c].append(board[r][c])
                sqre_map[(r//3,c//3)].append(board[r][c])
                
        return True
