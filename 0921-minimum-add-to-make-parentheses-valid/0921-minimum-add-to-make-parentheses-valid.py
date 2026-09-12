class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        moves = 0
        
        for char in s:
            if char == '(':
                open_brackets += 1
            elif char == ')':
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    moves += 1  # Unmatched closing bracket requires an insertion
                    
        return moves + open_brackets