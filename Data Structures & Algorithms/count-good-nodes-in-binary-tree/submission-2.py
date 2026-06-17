# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, peak):
            if node is None:
                return 0
            good = 0
            if node.val >= peak:
                good = 1
            peak = max(peak,node.val)
            left = dfs(node.left, peak)
            right = dfs(node.right, peak)
            return good + left + right
        return dfs(root, float("-inf"))
