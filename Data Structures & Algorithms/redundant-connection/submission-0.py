class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            if node in visit:
                return True
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()  # Reset visited nodes for each new edge
            if dfs(u, -1):  # Start DFS from one endpoint of the current edge
                return [u, v]
                
        return []
