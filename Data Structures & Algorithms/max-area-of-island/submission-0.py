class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r, c):
            nonlocal largest
            area = 1
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            while q:
                rq, cq = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + rq, dc + cq
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0:
                        continue
                    q.append((nr,nc))
                    area += 1
                    grid[nr][nc] = 0
            largest = max(largest, area)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    bfs(r,c)

        return largest
                

