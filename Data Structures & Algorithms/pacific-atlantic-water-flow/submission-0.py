class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])

        # Create two hash sets for the two oceans
        pacific = set()
        atlantic = set()

        # Directions for the 4 possible moves: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS function to explore the cells
        def bfs(starts, visited):
            q = deque(starts)
            while q:
                r, c = q.popleft()
                visited.add((r, c))  # Mark the current cell as visited
                # Explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))

        # Initialize BFS from the Pacific edge (first row and first column)
        pacific_starts = [(0, i) for i in range(n)] + [(i, 0) for i in range(m)]
        bfs(pacific_starts, pacific)

        # Initialize BFS from the Atlantic edge (last row and last column)
        atlantic_starts = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m)]
        bfs(atlantic_starts, atlantic)

        # The result will be the intersection of both sets
        result = list(pacific & atlantic)
        return result
            