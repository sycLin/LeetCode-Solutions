# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root == None:
            return ret
        listt = []
        listt.append(root)
        while len(listt) > 0:
            ret.append([node.val for node in listt])
            new_listt = []
            for node in listt:
                if node.left:
                    new_listt.append(node.left)
                if node.right:
                    new_listt.append(node.right)
            listt = new_listt
        return ret[::-1]
