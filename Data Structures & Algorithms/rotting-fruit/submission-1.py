class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_count = 0
        q = deque()
        time = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    orange_count+=1 
                elif grid[i][j] == 2:
                    q.append((i,j))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while q and orange_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        orange_count -= 1
            time += 1
        
        return time if orange_count == 0 else -1



