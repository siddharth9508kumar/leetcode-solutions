class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Count the frequency of set bits at each bit position
        bit_counts = [0] * 30
        for num in nums:
            for i in range(30):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        # Construct the k numbers to maximize their values
        res_nums = [0] * k
        for i in range(30):
            if bit_counts[i] > 0:
                # Distribute the available set bits to the first bit_counts[i] numbers
                for j in range(min(k, bit_counts[i])):
                    res_nums[j] |= (1 << i)
                    
        # Calculate the sum of squares modulo 10^9 + 7
        total_sum = 0
        for num in res_nums:
            total_sum = (total_sum + num * num) % MOD
            
        return total_sum