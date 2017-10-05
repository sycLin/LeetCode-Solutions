# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret, retD = self.myIsBalanced(root)
        return ret

    def myIsBalanced(self, root):
        # terminal condition
        if not root:
            return True, 0
        leftIsBalanced, leftDepth = self.myIsBalanced(root.left)
        rightIsBalanced, rightDepth = self.myIsBalanced(root.right)
        ret = leftIsBalanced and rightIsBalanced and (-1 <= (leftDepth - rightDepth) <= 1)
        retD = max(leftDepth, rightDepth) + 1
        return ret, retD
