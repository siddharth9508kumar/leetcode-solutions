class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        negative = (dividend < 0) ^ (divisor < 0)
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        while abs_dividend >= abs_divisor:
            temp = abs_divisor
            multiple = 1
            while abs_dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            abs_dividend -= temp
            quotient += multiple
            
        res = -quotient if negative else quotient
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res