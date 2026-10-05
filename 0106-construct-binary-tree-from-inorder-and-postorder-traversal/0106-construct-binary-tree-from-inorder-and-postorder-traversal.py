# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder or not postorder:
            return None
        
        # The last element in postorder is the root of the current tree/subtree
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Index of root in inorder traversal
        idx = inorder.index(root_val)
        
        # Slice inorder into left and right subtrees
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx + 1:]
        
        # Recursively build right subtree first, then left subtree
        root.right = self.buildTree(inorder_right, postorder)
        root.left = self.buildTree(inorder_left, postorder)
        
        return root