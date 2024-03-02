class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1  # Pointers for 0s and 2s
        curr = 0  # Pointer for traversing the array
        
        # Traverse the array until the pointers meet
        while curr <= right:
            if nums[curr] == 0:  # If current element is 0, swap with left pointer
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1  # Move left pointer to the right
                curr += 1  # Move current pointer to the right
            elif nums[curr] == 2:  # If current element is 2, swap with right pointer
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1  # Move right pointer to the left
            else:
                curr += 1  # If current element is 1, move current pointer to the right
