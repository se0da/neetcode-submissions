class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        components = 0

        def dfs(node):
            # Visit all neighbors recursively
            for neighbor in adj[node]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    dfs(neighbor)

        # Iterate over all nodes
        for node in range(n):
            if node not in visit:
                # New component found
                components += 1
                visit.add(node)
                dfs(node)
        
        return components