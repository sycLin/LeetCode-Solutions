class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mapping, rev_mapping = {}, {}
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        for i, character in enumerate(pattern):
            if character not in mapping.keys() and words[i] not in rev_mapping.keys():
                mapping[character] = words[i]
                rev_mapping[words[i]] = character
            else:
                keyExists = (character in mapping.keys()) and (words[i] in rev_mapping.keys())
                if not keyExists:
                    return False
                if words[i] == mapping[character] and character == rev_mapping[words[i]]:
                    pass
                else:
                    return False
        return True

        
