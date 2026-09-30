# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        max_width = 0
        # Queue stores pairs of (node, index)
        queue = deque([(root, 0)])
        
        while queue:
            level_size = len(queue)
            _, first_index = queue[0]
            _, last_index = queue[-1]
            
            # Width is the difference between the first and last position indices + 1
            max_width = max(max_width, last_index - first_index + 1)
            
            for _ in range(level_size):
                node, index = queue.popleft()
                # Normalize index to avoid huge numbers
                normalized_index = index - first_index
                
                if node.left:
                    queue.append((node.left, 2 * normalized_index))
                if node.right:
                    queue.append((node.right, 2 * normalized_index + 1))
                    
        return max_width