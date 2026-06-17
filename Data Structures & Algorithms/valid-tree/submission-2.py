class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= len(edges):
            return False

        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visit = set()

        def dfs(cur, parent):
            if cur in visit:
                return False
            
            visit.add(cur)
            for nei in adj[cur]:
                if nei == parent:
                    continue
                
                if not dfs(nei, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n