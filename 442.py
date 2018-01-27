class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = set()
        for i, num in enumerate(nums):
            index = abs(num) - 1
            if nums[index] < 0:
                ret.add(index + 1)
            else:
                nums[index] = -nums[index]
        return list(ret)
            
        