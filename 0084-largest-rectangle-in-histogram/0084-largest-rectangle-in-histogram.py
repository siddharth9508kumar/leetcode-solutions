class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  
        
        for i, h in enumerate(heights):
            # Maintain monotonic increasing stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # If stack is empty, the rectangle extends all the way to index 0
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        # Process remaining bars in stack against the total length
        n = len(heights)
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        return max_area