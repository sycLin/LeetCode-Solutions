class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # method: using Python set data structure (kinda like cheating)
        # => ACCEPT
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
        """
        # method: sort and then go-through
        # => ACCEPT
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        index1, index2 = 0, 0
        ret = []
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                if len(ret) > 0 and nums1[index1] != ret[-1]:
                    ret.append(nums1[index1])
                index1 += 1
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        return ret
