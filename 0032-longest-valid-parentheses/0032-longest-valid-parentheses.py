class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to serve as the boundary index
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                # Store the index of the opening bracket
                stack.append(i)
            else:
                # Pop the last open bracket index or boundary
                stack.pop()

                if not stack:
                    # Current ')' is unmatched; push its index as the new boundary
                    stack.append(i)
                else:
                    # Calculate length from current index to the previous boundary/unmatched index
                    max_length = max(max_length, i - stack[-1])

        return max_length