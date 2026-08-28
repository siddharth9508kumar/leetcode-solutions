class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate total hours spent at speed `mid`
            total_hours = sum((pile + mid - 1) // mid for pile in piles)
            
            if total_hours <= h:
                right = mid  # Try to find a smaller speed
            else:
                left = mid + 1  # Speed is too slow, increase it
                
        return left

        