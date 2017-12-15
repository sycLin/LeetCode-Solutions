class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        #
        # transform to counting array
        #
        prev_ch, counter = s[0], 1
        counting = []
        for ch in s[1:]:
            if ch == prev_ch:
                counter += 1
            else:
                counting.append(counter)
                counter = 1
            prev_ch = ch
        counting.append(counter)
        #
        # main
        #
        total = 0
        for i in range(len(counting) - 1):
            total += min(counting[i], counting[i+1])
        return total
        