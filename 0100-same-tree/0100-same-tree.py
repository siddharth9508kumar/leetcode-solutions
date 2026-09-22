# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Both nodes are None -> trees are identical up to this branch
        if not p and not q:
            return True
        
        # One node is None and the other isn't -> trees are structurally different
        if not p or not q:
            return False
        
        # Values don't match -> trees are different
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)