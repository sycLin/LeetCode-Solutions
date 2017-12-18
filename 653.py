# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        inOrderArray = self.getInOrder(root)
        l, r = 0, len(inOrderArray) - 1
        while l < r:
            current = inOrderArray[l] + inOrderArray[r]
            if current == k:
                return True
            elif current < k:
                l += 1
            else:
                r -= 1
        return False
    
    def getInOrder(self, root):
        if root is None:
            return []
        ret = []
        return self.getInOrder(root.left) + [root.val] + self.getInOrder(root.right)
        