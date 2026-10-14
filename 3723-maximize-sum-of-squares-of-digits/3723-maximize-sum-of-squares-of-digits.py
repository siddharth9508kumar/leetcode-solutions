class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if the sum is within the possible range [0, 9 * num]
        if sum < 0 or sum > 9 * num:
            return ""
        
        ans = []
        for i in range(num):
            # Take the maximum possible digit for the current position
            cur = min(9, sum)
            ans.append(str(cur))
            sum -= cur
            
        # If any sum is left over, it's invalid
        if sum > 0:
            return ""
            
        return "".join(ans)