class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        index1, index2 = 0, 0
        ret = []
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                ret.append(nums1[index1])
                index1, index2 = index1 + 1, index2 + 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        return ret
        
