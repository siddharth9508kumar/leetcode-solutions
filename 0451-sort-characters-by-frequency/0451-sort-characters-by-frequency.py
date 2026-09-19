from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count frequency of each character
        counts = Counter(s)
        
        # Step 2: Sort characters by frequency (descending) and reconstruct
        res = []
        for char, freq in counts.most_common():
            res.append(char * freq)
            
        return "".join(res)