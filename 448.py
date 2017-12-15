class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #
        # Method #1
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Result: ACCEPTED, 370 ms
        #
        n = len(nums)
        counting = [0 for i in range(n)]
        for num in nums:
            counting[num - 1] += 1
        return [i+1 for i in range(n) if counting[i] == 0]
        #
        # Method #2
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Result: ACCEPTED, 340 ms
        #
        n = len(nums)
        d = {}
        for num in nums:
            d[num - 1] = True
        return [i + 1 for i in range(n) if d.get(i) == None]
        