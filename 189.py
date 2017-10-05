class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(l, start, end):
            while start < end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1
        k = k % (len(nums))
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums) - 1)

        
