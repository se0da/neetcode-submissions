# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxV):
            good = 0
            if root is None:
                return 0
            if root.val >= maxV:
                good = 1
            maxV = max(maxV, root.val)
            left = dfs(root.left, maxV)
            right = dfs(root.right, maxV)
            return left + right + good
        return dfs(root, float("-inf"))

