# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def buildTree(
      self, preorder: list[int], inorder: list[int]
  ) -> TreeNode | None:
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = 0

    def helper(left: int, right: int) -> TreeNode | None:
      nonlocal pre_idx

      if left > right:
        return None

      root_val = preorder[pre_idx]
      root = TreeNode(root_val)
      pre_idx += 1

      inorder_idx = inorder_map[root_val]

      root.left = helper(left, inorder_idx - 1)
      root.right = helper(inorder_idx + 1, right)

      return root

    return helper(0, len(inorder) - 1)
    