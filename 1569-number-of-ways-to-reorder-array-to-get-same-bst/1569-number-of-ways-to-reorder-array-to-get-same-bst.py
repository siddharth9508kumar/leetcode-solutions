import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        if len(nums) <= 2:
            return 0
        
        root = nums[0]
        left = [x for x in nums[1:] if x < root]
        right = [x for x in nums[1:] if x > root]
        
        return (math.comb(len(left) + len(right), len(left)) * (self.numOfWays(left) + 1) * (self.numOfWays(right) + 1) - 1) % MOD