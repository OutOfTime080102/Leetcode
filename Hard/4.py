class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            return (self.findKth(nums1, nums2, total_length // 2) + self.findKth(nums1, nums2, total_length // 2 - 1)) / 2.0
        else:
            return self.findKth(nums1, nums2, total_length // 2)

    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])

        mid1, mid2 = len(nums1) // 2, len(nums2) // 2
        if mid1 + mid2 < k:
            if nums1[mid1] > nums2[mid2]:
                return self.findKth(nums1, nums2[mid2 + 1:], k - mid2 - 1)
            else:
                return self.findKth(nums1[mid1 + 1:], nums2, k - mid1 - 1)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.findKth(nums1[:mid1], nums2, k)
            else:
                return self.findKth(nums1, nums2[:mid2], k)
