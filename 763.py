import string

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 0:
            return [0,]
        #
        # get range for each of the lowercase letters
        #
        ranges = []
        for c in string.lowercase:
            start, end = None, None
            for i in range(len(S)):
                if S[i] == c:
                    start = i if start is None else start
                    end = i
            if start is not None:
                ranges.append([start, end])
        #
        # merge those ranges
        #
        ranges = sorted(ranges, key=lambda r: (r[0], r[1]))
        
        merged_ranges = []
        current = None
        for r in ranges:
            if current is None:
                current = r
            elif r[0] < current[1]:
                current[1] = max(current[1], r[1])
            else:
                merged_ranges.append(current)
                current = r
        if current:
            merged_ranges.append(current)
        return map(lambda r: r[1] - r[0] + 1, merged_ranges)