# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def flatten(self, root: TreeNode | None) -> None:
    """Do not return anything, modify root in-place instead."""
    curr = root

    while curr:
      if curr.left:
        # Find the rightmost node of the left subtree
        prev = curr.left
        while prev.right:
          prev = prev.right

        # Rewire: attach original right subtree to the rightmost node of left subtree
        prev.right = curr.right
        # Move left subtree to right and nullify left child
        curr.right = curr.left
        curr.left = None

      # Move to the next node in the right chain
      curr = curr.right