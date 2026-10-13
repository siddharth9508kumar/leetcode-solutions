class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Square each element and sort them in ascending order
        squared = sorted([x * x for x in nums])
        n = len(squared)
        
        # Subtract the first half (smaller squared values) and add the second half (larger squared values)
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans -= squared[i]
            else:
                ans += squared[i]
                
        return ans