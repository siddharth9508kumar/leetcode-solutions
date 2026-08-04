class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1

        # 1. Find the FIRST occurrence
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                first = mid
                end = mid - 1  # Keep searching left to find an earlier index
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        # 2. Find the LAST occurrence
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                last = mid
                start = mid + 1  # Keep searching right to find a later index
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return [first, last]
                

