"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = defaultdict()

        if node is None:
            return None

        def dfs(node):
            if node in mp:
                return
            mp[node] = Node(node.val)
            for nei in node.neighbors:
                dfs(nei)
            
        dfs(node)
        for key, value in mp.items():
            for nei in key.neighbors:
                value.neighbors.append(mp[nei])
        
        return mp[node]