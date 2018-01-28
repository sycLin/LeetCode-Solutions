# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        # perform BFS
        q = [root]
        ret = []
        while len(q) > 0:
            M = float("-INF")
            new_q = []
            while len(q) > 0:
                node = q.pop()
                M = max(M, node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            ret.append(M)
            q = new_q
        return ret