class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index1, index2 = m - 1, n - 1
        index = m + n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[index] = nums1[index1]
                index, index1 = index - 1, index1 - 1
            else:
                nums1[index] = nums2[index2]
                index, index2 = index - 1, index2 - 1
        if index2 >= 0:
            nums1[:index2+1] = nums2[:index2+1]
        
