class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent):
            if node in cur:
                return False
            cur.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
            cur = set()
            if not dfs(x,-1):
                return [x,y]
        
        
