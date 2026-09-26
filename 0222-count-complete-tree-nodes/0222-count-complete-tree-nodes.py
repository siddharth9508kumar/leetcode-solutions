# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        # Calculate height along the leftmost path
        left_h = 0
        curr = root
        while curr:
            left_h += 1
            curr = curr.left

        # Calculate height along the rightmost path
        right_h = 0
        curr = root
        while curr:
            right_h += 1
            curr = curr.right

        # If left and right heights match, it is a perfect binary tree
        if left_h == right_h:
            return (1 << left_h) - 1

        # Recursively count nodes in left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)