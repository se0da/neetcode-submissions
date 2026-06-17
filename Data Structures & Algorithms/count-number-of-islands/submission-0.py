class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #implement using a bfs to mark all the 1s to 0s 
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(directions, grid, i,j)
                    islands+=1
        return islands

    def bfs(self, directions, grid, r, c):
        grid[r][c] = "0"
        q = deque()
        q.append((r,c))
        while q:
            row, col = q.popleft()
            for rowd, cold in directions:
                nr, nc = rowd + row, cold + col
                if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "0"):
                    continue
                q.append((nr,nc))
                grid[nr][nc] = "0"
            





