class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(len(edges)+1)]

        def dfs(node, parent):
            if node in visit:
                return True
            visit.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    return True
            return False

        for u, v in edges:
            visit = set()
            adj_list[u].append(v)
            adj_list[v].append(u)
            if dfs(u, -1):
                return [u,v]

        return []
        
