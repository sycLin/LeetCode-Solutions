class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # method: O(n^2)
        # => TLE
        """
        ret = [False for i in range(len(nums))]
        ret[0] = True
        for i in range(len(nums)):
            # print "nums[%d] = %d" % (i, nums[i])
            if ret[i]:
                for j in range(nums[i]):
                    try:
                        # print "setting %d to true" % (i + j + 1)
                        ret[i + j + 1] = True
                    except:
                        pass
        # print ret
        return ret[-1]
        """
        # method: O(n)
        # => ACCEPT
        count = 1
        for number in nums:
            if count - 1 < 0:
                return False
            count = max(number, count - 1)
        return True
