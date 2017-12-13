# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def fix(self, node, fromParent):
        if node is None:
            return 0
        rightSum = self.fix(node.right, fromParent)
        o = node.val
        node.val += (rightSum + fromParent)
        leftSum = self.fix(node.left, node.val)
        return rightSum + leftSum + o
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.fix(root, 0)
        return root
        