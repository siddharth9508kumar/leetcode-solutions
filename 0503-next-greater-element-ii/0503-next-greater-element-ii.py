class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # Stores indices of elements in decreasing order

        # Traverse the array twice to handle circular behavior
        for i in range(2 * n):
            curr = nums[i % n]
            
            # Pop elements from stack that are smaller than the current element
            while stack and nums[stack[-1]] < curr:
                idx = stack.pop()
                res[idx] = curr
                
            # Only push indices from the first pass
            if i < n:
                stack.append(i)
                
        return res