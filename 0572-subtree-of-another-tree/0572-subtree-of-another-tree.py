# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        # If subRoot is None, an empty tree is always a subtree
        if not subRoot:
            return True
        # If root is None but subRoot isn't, subRoot can't be a subtree
        if not root:
            return False

        # Check if trees are identical starting at the current node
        if self.isSameTree(root, subRoot):
            return True

        # Otherwise, check left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)