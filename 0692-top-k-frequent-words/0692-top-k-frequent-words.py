from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # Count frequencies
        count = Counter(words)
        
        # Sort by frequency descending
        sorted_words = sorted(count.keys(), key=lambda w: (-count[w], w))
        
        # Return worts
        return sorted_words[:k]