class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mini = max(weights)
        maxi = sum(weights)

        while mini < maxi:
            mid = (mini + maxi) // 2
            
            # Check feasibility directly inline
            required_days = 1
            current_day_weight = 0
            
            for w in weights:
                if current_day_weight + w > mid:
                    required_days += 1
                    current_day_weight = 0
                current_day_weight += w
            
            # Adjust binary search boundaries
            if required_days <= days:
                maxi = mid
            else:
                mini = mid + 1

        return mini