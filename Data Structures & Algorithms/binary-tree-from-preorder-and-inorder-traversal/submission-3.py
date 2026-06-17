# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {v : i for i, v in enumerate(inorder)}
        
        def dfs(left_pre, right_pre, left_in, right_in):
            if left_pre > right_pre:
                return None

            node_val = preorder[left_pre]
            node = TreeNode(node_val)
            node_index_inorder = lookup[node_val]
            
            node.left = dfs(left_pre + 1, node_index_inorder - left_in + left_pre, left_in, node_index_inorder - 1)
            node.right = dfs(left_pre + node_index_inorder - left_in + 1, right_pre, node_index_inorder + 1, right_in)
            
        
            return node
        
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)
