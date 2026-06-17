# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        res = []

        while q:
            curr_level = []
            for var in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr_level)
        res2 = [[] for _ in range(len(res))]
        for i in range(len(res)):
            res2[i] = res[i][-1]
        
        return res2