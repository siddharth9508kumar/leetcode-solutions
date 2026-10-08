# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # Base case: if we reach an empty spot, insert the new node here
        if not root:
            return TreeNode(val)
        
        # If the value to insert is smaller, go to the left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # If the value to insert is larger, go to the right subtree
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root