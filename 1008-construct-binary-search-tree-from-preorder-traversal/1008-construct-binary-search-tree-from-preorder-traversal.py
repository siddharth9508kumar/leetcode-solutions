# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for val in preorder[1:]:
            node = TreeNode(val)
            # If the value is smaller, it's the left child of the current stack top
            if val < stack[-1].val:
                stack[-1].left = node
            else:
                # Otherwise, pop until we find the right parent node
                parent = None
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node
            
            stack.append(node)
            
        return root