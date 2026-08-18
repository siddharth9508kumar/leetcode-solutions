class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Helper function to count occurrences of a number in nums
        def count_freq(target: int) -> int:
            total = 0
            for num in nums:
                if num == target:
                    total += 1
            return total

        # Case 1: k = 1
        # Return the largest element that appears exactly once in the entire array
        if k == 1:
            ans = -1
            for num in nums:
                if count_freq(num) == 1:
                    if num > ans:
                        ans = num
            return ans
        
        # Case 2: k = n
        # There's only 1 subarray, so return the maximum element in nums
        if k == n:
            ans = nums[0]
            for num in nums:
                if num > ans:
                    ans = num
            return ans
        
        # Case 3: 1 < k < n
        # Only the boundary elements (nums[0] and nums[-1]) can appear in exactly 1 subarray
        ans = -1
        if count_freq(nums[0]) == 1:
            ans = nums[0]
        if count_freq(nums[-1]) == 1:
            if nums[-1] > ans:
                ans = nums[-1]
                
        return ans