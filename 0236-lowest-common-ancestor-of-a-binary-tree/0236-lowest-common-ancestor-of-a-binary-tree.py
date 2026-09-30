# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None, or if root is one of p or q
        if not root or root == p or root == q:
            return root
        
        # Recursively search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in left and right subtrees respectively, root is the LCA
        if left and right:
            return root
            
        # Otherwise, return whichever subtree returned a non-null node
        return left if left else right