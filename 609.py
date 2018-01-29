from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        # map content to files
        mapContent2Files = defaultdict(list)
        
        for dInfo in paths:
            tokens = dInfo.split()
            dPath = tokens[0]
            for fInfo in tokens[1:]:
                fName = fInfo.split("(")[0]
                content = fInfo.split("(")[1][:-1]
                mapContent2Files[content].append(dPath + "/" + fName)
        
        ret = []
        for k, v in mapContent2Files.iteritems(): # note: python 3.x does not have iteritems()
            if len(v) > 1:
                ret.append(v)
        return ret