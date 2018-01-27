class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        while len(ret) < num + 1:
            for i in range(len(ret)):
                ret.append(ret[i] + 1)
        return ret[:num + 1]
        