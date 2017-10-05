class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        rows = [[1]]
        while (numRows - 1) > 0:
            lastRow = rows[-1]
            newRow = [1]
            for i in range(1, len(lastRow)):
                newRow.append(lastRow[i-1] + lastRow[i])
            newRow.append(1)
            rows.append(newRow)
            numRows -= 1
        return rows
        
