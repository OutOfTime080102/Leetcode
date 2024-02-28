class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0:
            sum_bits = carry
            
            if i >= 0:
                sum_bits += int(a[i])
                i -= 1
            if j >= 0:
                sum_bits += int(b[j])
                j -= 1
            
            result += str(sum_bits % 2)
            carry = sum_bits // 2
        
        if carry:
            result += str(carry)
        
        return result[::-1]
