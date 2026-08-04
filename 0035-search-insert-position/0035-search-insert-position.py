class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid  # Found the target, return its index
            elif nums[mid] < target:
                start = mid + 1  # Target is in the right half
            else:
                end = mid - 1    # Target is in the left half
                
        return start       # If target is not found, 'start' will be the correct insert position