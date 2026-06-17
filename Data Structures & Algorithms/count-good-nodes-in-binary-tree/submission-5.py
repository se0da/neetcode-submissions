# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_so_far):
            if root is None:
                return 0
            good = 0
            if root.val >= max_so_far:
                max_so_far = root.val
                good = 1
            
            left = dfs(root.left, max_so_far)
            right = dfs(root.right, max_so_far)

            return left + right + good
        
        return dfs(root, float("-inf"))
        
