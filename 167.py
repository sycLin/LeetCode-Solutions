class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1, index2 = 0, len(numbers) - 1
        while index1 < index2:
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
            else:
                return [index1 + 1, index2 + 1]
        return None # should not be here, exactly 1 solution guaranteed
