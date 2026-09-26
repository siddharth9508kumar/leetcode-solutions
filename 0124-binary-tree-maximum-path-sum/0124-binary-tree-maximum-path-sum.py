# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = float('-inf')

        def max_gain(node: TreeNode | None) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Recursively compute the maximum path sum starting from left and right children
            # Ignore negative sums by clamping to 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Price of the path where the current node acts as the root/highest point of the path
            current_path_sum = node.val + left_gain + right_gain

            # Update global maximum sum
            max_sum = max(max_sum, current_path_sum)

            # Return the maximum gain the parent node can obtain by extending the path through this node
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return max_sum