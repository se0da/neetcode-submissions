# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        res = []
        q.append(root)

        while q:
            cur = []
            for _ in range(len(q)):
                pop = q.popleft()
                cur.append(pop.val)
                if pop.left: q.append(pop.left)
                if pop.right: q.append(pop.right)
            res.append(cur[-1])
        return res
        