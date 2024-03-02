class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1  # Check if the least significant bit is set
            n >>= 1         # Shift n to the right by 1 bit
        return count
