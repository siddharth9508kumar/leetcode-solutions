class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Maintain a monotonically increasing stack
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0 remains, truncate from the right
        if k > 0:
            stack = stack[:-k]
        
        # Convert to string and remove leading zeros
        result = "".join(stack).lstrip("0")
        
        return result if result else "0"