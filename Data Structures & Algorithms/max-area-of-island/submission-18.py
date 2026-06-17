class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            cur = 1
            cur += dfs(r+1,c)
            cur += dfs(r-1,c)
            cur += dfs(r,c+1)
            cur += dfs(r,c-1)

            return cur

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    res = max(res, area)

        return res
