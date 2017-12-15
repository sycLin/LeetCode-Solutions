# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self._maxPathSum(root))
    
    
    def _maxPathSum(self, root):
        """
        :rtype: (int, int) <= (canConcat, cannotConcat)
        """
        if root is None:
            return 0, float('-INF')
        lcan, lcannot = self._maxPathSum(root.left)
        rcan, rcannot = self._maxPathSum(root.right)
        canConcat = root.val + max(lcan, rcan, 0)
        cannotConcat = max(lcannot, rcannot, root.val + lcan + rcan, root.val + max(lcan, rcan))
        print(root.val, canConcat, cannotConcat)
        return canConcat, cannotConcat
        