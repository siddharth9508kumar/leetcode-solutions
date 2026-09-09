class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # 1. Extract the encoded string inside brackets
                decoded_str = []
                while stack and stack[-1] != '[':
                    decoded_str.append(stack.pop())
                decoded_str.reverse()
                
                # Pop the opening bracket '['
                stack.pop()

                # 2. Extract the multi-digit number k
                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                k.reverse()
                count = int("".join(k))

                # 3. Repeat string k times and push back to stack
                stack.append("".join(decoded_str) * count)

        return "".join(stack)