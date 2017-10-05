class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # method: use the formula
        if rowIndex <= 0:
            return [1]
        ret = [1]
        numerator = 1
        denominator = 1
        for i in range(1, rowIndex / 2 + 1):
            numerator *= (rowIndex - (i - 1))
            denominator *= (i)
            ret.append(numerator / denominator)
        if rowIndex % 2 == 1:
            return ret + ret[::-1]
        else:
            return ret + ret[-2::-1]

        
