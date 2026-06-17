class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            is_good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            count_left = dfs(node.left, new_max)
            count_right = dfs(node.right, new_max)

            return is_good + count_left + count_right

        return dfs(root, -float('inf')) 