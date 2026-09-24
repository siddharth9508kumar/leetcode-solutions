class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            
            # Calculate the sum of digits for nums[i]
            digit_sum = sum(int(digit) for digit in str(nums[i]))
            
            # Check if the digit sum equals the index i
            if digit_sum == i:
                return i
                
        return -1