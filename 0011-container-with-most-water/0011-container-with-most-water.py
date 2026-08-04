class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        
        while l < r:
            # Calculate current water capacity
            current_height = min(height[l], height[r])
            width = r - l
            current_area = current_height * width
            
            # Update maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area