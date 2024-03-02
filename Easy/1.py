class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of elements seen so far
        num_indices = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement (target - num)
            complement = target - num
            
            # If the complement is in the dictionary, return the indices
            if complement in num_indices:
                return [num_indices[complement], i]
            
            # Otherwise, store the current number and its index in the dictionary
            num_indices[num] = i
        
        # If no solution is found, return an empty list
        return []
