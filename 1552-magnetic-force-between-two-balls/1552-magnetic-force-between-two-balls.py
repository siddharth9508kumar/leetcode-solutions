class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        l = 1
        r = position[-1] - position[0]
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            
            # Inline check to see if distance 'mid' is feasible
            count = 1
            last = position[0]
            for pos in position[1:]:
                if pos - last >= mid:
                    count += 1
                    last = pos
                    if count == m:
                        break
            
            if count >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans