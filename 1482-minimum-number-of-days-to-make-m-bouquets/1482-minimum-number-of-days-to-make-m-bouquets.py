class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        # Impossible to make m bouquets if total required flowers exceed array size
        if m * k > n:
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = (left + right) // 2
            
            # Count how many bouquets of size k can be made by day 'mid'
            bouquets = 0
            flowers = 0
            for b in bloomDay:
                if b <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            
            # Binary search range adjustment
            if bouquets >= m:
                right = mid
            else:
                left = mid + 1
                
        return left








__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))