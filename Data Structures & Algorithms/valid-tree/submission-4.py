class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cur = set()
        done = set()
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        def dfs(node,parent):
            if node in cur:
                return False
            if node in done:
                return True
            cur.add(node)
            for x in adj_list[node]:
                if x == parent:
                    continue
                if not dfs(x,node):
                    return False
            cur.remove(node)
            done.add(node)
            return True
        
        return dfs(0,-1) and len(done) == n
