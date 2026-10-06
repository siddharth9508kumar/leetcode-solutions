# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # preorder[1] is the root of the left subtree
        # Find its size using its position in postorder
        left_size = postorder.index(preorder[1]) + 1
        
        # Recursively assign left and right subtrees
        root.left = self.constructFromPrePost(preorder[1 : left_size + 1], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[left_size + 1 :], postorder[left_size : -1])
        
        return root