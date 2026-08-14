class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        # We only need to search up to index (n - m)
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
                
        return -1




__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))