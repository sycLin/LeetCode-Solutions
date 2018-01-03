# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            # the end
            return None
        if t1 is None:
            # only t2
            n = TreeNode(t2.val)
            n.left = self.mergeTrees(None, t2.left)
            n.right = self.mergeTrees(None, t2.right)
        elif t2 is None:
            # only 1
            n = TreeNode(t1.val)
            n.left = self.mergeTrees(t1.left, None)
            n.right = self.mergeTrees(t1.right, None)
        else:
            # both t1 and t2
            n = TreeNode(t1.val + t2.val)
            n.left = self.mergeTrees(t1.left, t2.left)
            n.right = self.mergeTrees(t1.right, t2.right)
        return n
        