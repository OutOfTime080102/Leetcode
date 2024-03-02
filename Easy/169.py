class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = None
        count = 0

        for num in nums:
            if count == 0:
                n = num
            count += (1 if num == n else -1)

        return n
