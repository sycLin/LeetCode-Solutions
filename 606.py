# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        l, r = self.tree2str(t.left), self.tree2str(t.right)
        me = str(t.val)
        ret = ""
        if l == r == "":
            ret = me
        elif r == "":
            ret = "%s(%s)" % (me, l)
        else:
            ret = "%s(%s)(%s)" % (me, l, r)
        return ret
        