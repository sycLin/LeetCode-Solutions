class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #
        # Method 1: sorting
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        # Result: ACCEPT (45 ms)
        #
        s = sorted([ord(ch) for ch in s])
        t = sorted([ord(ch) for ch in t])
        if len(t) == 1:
            return chr(t[0])
        for i in range(len(s)):
            if s[i] != t[i]:
                return chr(t[i])
        return chr(t[-1])
        #
        # Method 2: counting
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Result: ACCEPT (42 ms)
        #
        count1, count2 = [0 for i in range(26)], [0 for i in range(26)]
        for ch in s:
            count1[ord(ch) - ord('a')] += 1
        for ch in t:
            count2[ord(ch) - ord('a')] += 1
        for i in range(26):
            if count1[i] != count2[i]:
                return chr(i + ord('a'))
        
        