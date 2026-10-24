class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current = "1"
        
        # Build the sequence iteratively up to n
        for _ in range(n - 1):
            next_string = []
            i = 0
            while i < len(current):
                count = 1
                
                # Count consecutive identical characters
                while i + 1 < len(current) and current[i] == current[i + 1]:
                    count += 1
                    i += 1

                # Append the count followed by the digit
                next_string.append(str(count))
                next_string.append(current[i])
                i += 1
            current = "".join(next_string)
            
        return current