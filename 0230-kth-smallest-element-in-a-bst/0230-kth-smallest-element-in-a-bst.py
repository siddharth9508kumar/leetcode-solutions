# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        current = root
        
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the processed node from the stack
            current = stack.pop()
            
            # Decrement k as we visit each node in ascending order
            k -= 1
            if k == 0:
                return current.val
            
            # Move to the right subtree
            current = current.right