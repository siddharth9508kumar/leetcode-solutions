class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            # to check the sum
            if current_sum == target:
                return [left + 1, right + 1]  # Convert to 1-based indexing
            elif current_sum < target:
                left += 1  # Need a larger sum, move left pointer right
            else:
                right -= 1  # Need a smaller sum, move right pointer left