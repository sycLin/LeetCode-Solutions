class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        rev_mapping = {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if c1 not in mapping.keys():
                if c2 not in rev_mapping.keys():
                    # add mapping
                    mapping[c1] = c2
                    rev_mapping[c2] = c1
                else:
                    return False
            else:
                # check mapping
                if not c2 == mapping[c1]:
                    return False
        return True
