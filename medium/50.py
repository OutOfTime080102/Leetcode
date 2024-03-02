class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:  # Base case: x^0 = 1
            return 1
        
        if n < 0:  # If n is negative, compute the reciprocal and change n to positive
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:  # Exponentiation by squaring algorithm
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        
        return result
