# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sums = []
        
        def getAllSums(r):
            if r is None:
                return 0
            s = r.val + getAllSums(r.left) + getAllSums(r.right)
            sums.append(s)
            return s
        _ = getAllSums(root)
        
        # find the most frequency
        sums = sorted(sums)
        current, count = None, 0
        maxFrequency = 0
        for s in sums:
            if s == current:
                count += 1
            else:
                maxFrequency = max(maxFrequency, count)
                current = s
                count = 1
        maxFrequency = max(maxFrequency, count)
        
        # return all elements with maxFrequency
        ret = []
        current, count = None, 0
        for s in sums:
            if s == current:
                count += 1
            else:
                if current is not None and count == maxFrequency:
                    ret.append(current)
                current = s
                count = 1
        if current is not None and count == maxFrequency:
            ret.append(current)
        return ret
