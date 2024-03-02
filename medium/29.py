class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:  # Handle edge case when dividend is 0
            return 0

        # Handle overflow cases
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            quotient += multiple
            dividend -= temp_divisor

        return -quotient if negative else quotient
