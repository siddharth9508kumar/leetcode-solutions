class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0
        
        while i < n:
            found = False
            for j in range(i + k - 1, min(i + k + 1, n)):
                # Check if s[i..j] is a palindrome
                sub = s[i : j + 1]
                if sub == sub[::-1]:
                    ans += 1
                    i = j + 1  # Skip past this non-overlapping palindrome
                    found = True
                    break
            
            if not found:
                i += 1
                
        return ans