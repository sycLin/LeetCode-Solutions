# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetricList(self, listt):
        if len(listt) == 0 or len(listt) == 1:
            return True
        start, end = 0, len(listt)-1
        while start < end:
            if listt[start] != listt[end]:
                return False
            start, end = start + 1, end - 1
        return True
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        # Method 1: traverse layer 1 by 1
        # => TLE
        listt = []
        listt.append(root)
        while True:
            values = [node.val if node else None for node in listt]
            if not any(listt):
                break
            if not self.isSymmetricList(values):
                return False
            new_listt = []
            for node in listt:
                if node is None:
                    new_listt += [None, None]
                else:
                    new_listt += [node.left, node.right]
            listt = new_listt
        return True
        """
        # Method 2: recursive
        # => ACCEPT
        if root == None:
            return True
        def symmetric(node1, node2):
            if node1 == node2 == None:
                return True
            if node1 == None and node2 != None:
                return False
            if node1 != None and node2 == None:
                return False
            return (node1.val == node2.val) and symmetric(node1.left, node2.right) and symmetric(node1.right, node2.left)
        return symmetric(root.left, root.right)

        
