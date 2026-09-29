"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        # Start with the root node
        curr = root
        
        # Loop until we reach the leaf level
        while curr.left:
            # Traversal pointer for the current level
            head = curr
            
            while head:
                # Connection 1: Connect the left child to the right child of the same parent
                head.left.next = head.right
                
                # Connection 2: Connect the right child to the left child of the next node across parents
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node in the current level using the already established next pointers
                head = head.next
            
            # Move down to the left-most node of the next level
            curr = curr.left
            
        return root