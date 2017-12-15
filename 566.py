class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        input_size = len(nums) * len(nums[0])
        output_size = r * c
        if input_size != output_size:
            return nums
        # Version 1
        # time: 175 ms
        """
        flatten = sum(nums, [])
        ret = []
        counter = 0
        for _r in range(r):
            tmp = []
            for _c in range(c):
                tmp.append(flatten[counter])
                counter += 1
            ret.append(tmp)
        return ret
        """
        # Version 2
        # time: 165 ms
        counter = 0
        old_row, old_col = len(nums), len(nums[0])
        ret = []
        for _r in range(r):
            tmp = []
            for _c in range(c):
                tmp.append(nums[counter / old_col][counter % old_col])
                counter += 1
            ret.append(tmp)
        return ret
