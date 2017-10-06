class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # method: O(2 * |s|)
        # => TLE
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        temporaryVowelContainer = []
        for c in s:
            if c in vowels:
                temporaryVowelContainer.append(c)
        ret = ""
        for i in range(len(s)):
            if s[i] in vowels:
                ret += temporaryVowelContainer.pop()
            else:
                ret += s[i]
        return ret
        """
        # method: O(|s|)
        # => ACCEPT
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = [c for c in s]
        left, right = 0, len(s) - 1
        while left < right:
            while left < len(s) and s[left] not in vowels:
                left += 1
            while right >= 0 and s[right] not in vowels:
                right -= 1
            if left >= right:
                break
            tmp = s[right]
            s[right] = s[left]
            s[left] = tmp
            left += 1
            right -= 1
        return "".join(s)
