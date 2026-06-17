"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque()
        q.append(node)
        o_to_n = {}
        while q:
            cur = q.popleft()
            if cur not in o_to_n:
                o_to_n[cur] = Node(cur.val)
            for nei in cur.neighbors:
                if nei not in o_to_n:
                    q.append(nei)
        
        for old, new in o_to_n.items():
            for og in old.neighbors:
                new.neighbors.append(o_to_n[og])
        return o_to_n[node]


