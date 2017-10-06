from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = defaultdict(int), defaultdict(int)
        for c in s:
            d1[c] += 1
        for c in t:
            d2[c] += 1
        for k in d1.keys():
            if d1[k] != d2[k]:
                return False
        for k in d2.keys():
            if d2[k] != d1[k]:
                return False
        return True
