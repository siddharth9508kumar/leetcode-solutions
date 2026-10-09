# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None, low=float('-inf'), high=float('inf')) -> bool:
        # An empty tree is a valid BST
        if not root:
            return True
        
        # The current node's value must be strictly between low and high
        if not (low < root.val < high):
            return False
        
        # Recursively validate left and right subtrees with updated boundaries
        return (self.isValidBST(root.left, low, root.val) and 
                self.isValidBST(root.right, root.val, high))