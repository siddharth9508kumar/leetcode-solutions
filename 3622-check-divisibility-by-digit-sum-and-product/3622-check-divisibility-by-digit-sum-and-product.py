class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        sum = 0
        product = 1
        for i in digits:
            sum = sum+i
            product = product *i
        if n % (sum + product) == 0 :
            return True
        else:
            return False


        