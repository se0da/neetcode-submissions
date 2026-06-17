class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)
            for x in adj_list[node]:
                if x == parent:
                    continue
                dfs(x,node)
            
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                res += 1
        return res
        