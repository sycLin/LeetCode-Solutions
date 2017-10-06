class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            summ = 0
            while num > 0:
                summ += num % 10
                num /= 10
            num = summ
        return num
        
