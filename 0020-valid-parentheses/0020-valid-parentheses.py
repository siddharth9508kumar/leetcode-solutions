class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in mapping:
                # Pop the top element if stack isn't empty, else assign a dummy value
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly matched
        return not stack