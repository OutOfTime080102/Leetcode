class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0
        
        # Move all non-zero numbers to the beginning of the array and count the number of non-zero numbers
        for num in nums:
            if num != 0:
                nums[non_zero_count] = num
                non_zero_count += 1
        
        # Assign 0 to the remaining elements from position non_zero_count to the end of the array
        for i in range(non_zero_count, len(nums)):
            nums[i] = 0
