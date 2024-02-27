class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums_set = set(nums)
        
        # Check for positive integers starting from 1 and return the first missing positive
        for i in range(1, n + 2):  # We consider up to n + 1 as the potential missing positive
            if i not in nums_set:
                return i
