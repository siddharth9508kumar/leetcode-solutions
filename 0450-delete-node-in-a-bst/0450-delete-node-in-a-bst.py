# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        
        # 1. Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found!
            
            # Case 1: The node has no left child (returns right child, whether None or a valid node)
            if not root.left:
                return root.right
            
            # Case 2: The node has no right child (returns left child)
            elif not root.right:
                return root.left
            
            # Case 3: The node has both children
            # Find the in-order successor (the minimum value in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
            
            # Replace the current node's value with the successor's value
            root.val = curr.val
            
            # Delete the successor from the right subtree
            root.right = self.deleteNode(root.right, curr.val)
            
        return root