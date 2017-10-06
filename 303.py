class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # get CDF
        self.cdf = []
        for i, number in enumerate(self.nums):
            if i == 0:
                self.cdf.append(number)
            else:
                self.cdf.append(self.cdf[-1] + number)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.cdf[j]
        return self.cdf[j] - self.cdf[i-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
