class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method 2: binary search-like
        # result: ACCEPTED
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            print("(l, r) = (%d, %d) => mid = %d" % (l, r, mid))
            isEvenTilMid = True if (mid - l) % 2 == 1 else False
            if nums[mid] == nums[mid - 1]:
                if isEvenTilMid:
                    # search right
                    l = mid + 1
                else:
                    # search left
                    r = mid
            elif nums[mid] == nums[mid + 1]:
                if isEvenTilMid:
                    # search left
                    r = mid - 1
                else:
                    # search right
                    l = mid
            else:
                return nums[mid]
        return nums[l]
        
        # method 1: Recursion
        # result: maximum recursion depth exceeded
        # terminal condition
        if len(nums) == 1:
            return nums[0]
        
        middle = len(nums) / 2
        if nums[middle - 1] == nums[middle]:
            # search the left
            return self.singleNonDuplicate(nums[:middle + 1])
        else:
            # search the right
            return self.singleNonDuplicate(nums[middle: ])
        