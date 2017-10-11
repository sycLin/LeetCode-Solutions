class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #   1 ~  26:   A -   Z => (   0 + 1) to (   0 + 26)
        #  27 ~  52:  AA -  AZ => (1*26 + 1) to (1*26 + 26)
        #  53 ~  78:  BA -  BZ => (2*26 + 1) to (2*26 + 26)
        # ...
        # 677 ~ 702:  ZA -  ZZ => (         26*26 + 1) to (         26*26 + 26)
        # 703 ~ 728: AAA - AAZ => (1*26*26 + 1*26 + 1) to (1*26*26 + 1*26 + 26)
        # 729 ~ 754: ABA - ABZ => (1*26*26 + 2*26 + 1) to (1*26*26 + 2*26 + 26)

        ret = []

        while n > 0:
            if n % 26 == 0:
                ret.insert(0, "Z")
                n -= 26
            else:
                ret.insert(0, "%s" % (chr(ord('A') + n % 26 - 1)))
                n -= (n % 26)
            n /= 26

        return "".join(ret)
