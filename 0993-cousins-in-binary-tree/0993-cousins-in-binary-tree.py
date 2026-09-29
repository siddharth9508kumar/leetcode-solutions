# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        if not root:
            return False
            
        queue = deque([(root, None)])  # (node, parent)
        
        while queue:
            x_parent = None
            y_parent = None
            
            # Process current level
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                
                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent
                
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            # Check conditions for current level
            if x_parent and y_parent:
                return x_parent != y_parent  # Same depth, different parents
            
            # If only one was found at this depth, they are not at the same level
            if x_parent or y_parent:
                return False
                
        return False