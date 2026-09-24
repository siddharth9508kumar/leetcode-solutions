# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        # If left subtree is empty, recurse on right subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
            
        # If right subtree is empty, recurse on left subtree
        if not root.right:
            return 1 + self.minDepth(root.left)
            
        # If both children exist, take the minimum of both paths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        