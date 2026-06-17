class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap to store value -> index relations for inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Helper function to recursively build the tree
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None
            
            # The root value is the first value in the preorder segment
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            
            # Get the root's index in the inorder traversal
            root_index = inorder_map[root_val]
            
            # Number of nodes in the left subtree
            left_size = root_index - in_left
            
            # Recursively build left and right subtrees
            root.left = helper(pre_left + 1, pre_left + left_size, in_left, root_index - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, root_index + 1, in_right)
            
            return root
        
        # Call the helper function with the full range of preorder and inorder
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
