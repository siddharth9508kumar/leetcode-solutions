import math
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        
        # Each of the first n-1 trains takes at least 1 hour.
        # If hour <= n - 1, it's impossible to reach on time.
        if hour <= n - 1:
            return -1
        
        left, right = 1, 10**7
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Calculate total time required at speed 'mid'
            total_time = 0.0
            for i in range(n - 1):
                total_time += math.ceil(dist[i] / mid)
            total_time += dist[-1] / mid  # Last ride does not need math.ceil
            
            if total_time <= hour:
                ans = mid
                right = mid - 1  # Try to find a smaller valid speed
            else:
                left = mid + 1   # Speed too slow, try faster
                
        return ans