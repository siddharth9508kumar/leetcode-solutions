class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left = num[:n // 2]
        right = num[n // 2:]
        
        sum_diff = 0
        q_diff = 0
        
        for char in left:
            if char == '?':
                q_diff += 1
            else:
                sum_diff += int(char)
                
        for char in right:
            if char == '?':
                q_diff -= 1
            else:
                sum_diff -= int(char)

        return (2 * sum_diff + 9 * q_diff) != 0