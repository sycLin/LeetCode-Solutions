class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        candidates = list(range(left, right + 1))
        return filter(lambda x: self.isDividingNumber(x), candidates)
    
    def isDividingNumber(self, x):
        digits = tuple(int(d) for d in str(x))
        if 0 in digits:
            return False
        for d in digits:
            if x % d != 0:
                return False
        return True