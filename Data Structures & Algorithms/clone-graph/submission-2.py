"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        visited = {}  # Hash map to store original node -> cloned node
        # Pass 1: Create all the cloned nodes
        q = deque()
        q.append(node)  # Use a queue for iterative traversal (BFS is easier for 2-pass)
        while q:
            curr = q.popleft()
            if curr not in visited:  # Only clone if not already visited
                visited[curr] = Node(curr.val) #create mapping of original to clone
                for neighbor in curr.neighbors:
                    q.append(neighbor)

        # Pass 2: Connect the neighbors of the cloned nodes
        for original_node, cloned_node in visited.items():
            for original_neighbor in original_node.neighbors:
                cloned_node.neighbors.append(visited[original_neighbor])

        return visited[node]  # Return the clone of the original starting node