class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # get plate_alphabet
        plate_alphabet = [0 for i in range(26)]
        for c in licensePlate.lower():
            if ord('a') <= ord(c) <= ord('z'):
                plate_alphabet[ord(c) - ord('a')] += 1

        # iterate the words
        answer, length = None, None
        for w in words:
            
            # speed up
            if answer is not None and len(w) >= length:
                continue

            # get word alphabet (w_alphabet)
            w_alphabet = [0 for i in range(26)]
            for c in w:
                order = ord(c) - ord('a')
                if 0 <= order < 26:
                    w_alphabet[order] += 1
            # check
            check = True
            for i in range(26):
                if w_alphabet[i] < plate_alphabet[i]:
                    check = False
            if check and (answer is None or len(w) < length):
                answer, length = w, len(w)

        return answer
