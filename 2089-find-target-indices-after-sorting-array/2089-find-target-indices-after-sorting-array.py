class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)
        index = []
        
        for i, val in enumerate(sorted_nums):
            if val == target:
                index.append(i)
                
        return index