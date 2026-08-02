class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate backwards through the array
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9, it becomes 0 and carry continues left
            digits[i] = 0

        # If all digits were 9, add 1 at the beginning (e.g., [9, 9] -> [1, 0, 0])
        return [1] + digits