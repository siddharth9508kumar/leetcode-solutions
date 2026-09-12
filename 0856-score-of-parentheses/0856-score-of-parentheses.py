class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Base layer score

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # If () score is 1, otherwise double inner score 2 * v
                stack[-1] += max(2 * v, 1)

        return stack[0]