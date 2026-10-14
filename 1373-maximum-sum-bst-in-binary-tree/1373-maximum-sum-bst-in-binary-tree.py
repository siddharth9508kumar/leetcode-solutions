# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode | None) -> int:
        self.max_sum = 0
        
        # Returns: (is_bst, min_val, max_val, sum_val)
        def dfs(node):
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            left_is_bst, left_min, left_max, left_sum = dfs(node.left)
            right_is_bst, right_min, right_max, right_sum = dfs(node.right)
            
            # Check if current node forms a valid BST
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_sum = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, current_sum)
                
                current_min = min(left_min, node.val)
                current_max = max(right_max, node.val)
                
                return True, current_min, current_max, current_sum
            
            # If not a BST, return False and dummy bounds
            return False, 0, 0, 0

        dfs(root)
        return self.max_sum