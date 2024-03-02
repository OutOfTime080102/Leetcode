class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define a variable to store the result
        result = 0
        
        # Define a variable to store the sign of the input integer
        sign = 1 if x >= 0 else -1
        
        # Take the absolute value of the input integer
        x = abs(x)
        
        # Reverse the digits of the input integer
        while x != 0:
            # Extract the last digit of x
            digit = x % 10
            
            # Update the result by adding the last digit
            result = result * 10 + digit
            
            # Update x by removing the last digit
            x //= 10
        
        # Apply the sign to the result
        result *= sign
        
        # Check for overflow
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
