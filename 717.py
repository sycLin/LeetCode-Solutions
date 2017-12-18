class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        s = "".join([str(b) for b in bits])
        t = s[:-1].split("0")[-1]
        if len(t) % 2 == 1:
            return False
        return True
        
        