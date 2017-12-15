class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # ugly code
        """
        d = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        ret = []
        for word in words:
            row = None
            success = True
            for character in word.upper():
                if character in d[0]:
                    _row = 0
                elif character in d[1]:
                    _row = 1
                else:
                    _row = 2
                if row is None:
                    row = _row
                if _row != row:
                    success = False
                    break
            if success:
                ret.append(word)
        return ret
        """
        # prettier code
        keyboard_rows = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        map2row = {} # map alphabet to row number
        for rowNum in range(len(keyboard_rows)):
            for character in keyboard_rows[rowNum]:
                map2row[character] = rowNum

        def criterion(word):
            if len(word) == 0:
                return True
            word = word.upper()
            return all(map(lambda character: map2row[character] == map2row[word[0]], word))
        
        return filter(criterion, words)