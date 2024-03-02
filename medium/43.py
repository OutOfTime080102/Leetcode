class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Convert the strings to integers
        num1_int = int(num1)
        num2_int = int(num2)
        
        # Multiply the integers
        result_int = num1_int * num2_int
        
        # Convert the result back to string and return
        return str(result_int)
