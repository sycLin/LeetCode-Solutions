class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sumShouldBe = (n + 1) * n / 2
        for num in nums:
            sumShouldBe -= num
        return sumShouldBe
