# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        
        def reverse_inorder(node):
            if not node:
                return
            
            # 1. Traverse the right subtree first (greater values)
            reverse_inorder(node.right)
            
            # 2. Update the running total and the current node's value
            self.total += node.val
            node.val = self.total
            
            # 3. Traverse the left subtree last (smaller values)
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root