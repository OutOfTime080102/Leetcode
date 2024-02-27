class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = 1
        result = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append((result, sign))
                result = 0
                sign = 1
            elif char == ')':
                prev_result, prev_sign = stack.pop()
                result += sign * num
                result *= prev_sign
                result += prev_result
                num = 0
        
        return result + sign * num
