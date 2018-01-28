# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # perform BFS
        q = [(root, 0)]
        current_leftmost = (None, None)
        while len(q) > 0:
            node, level = q.pop(0)
            # update current_leftmost
            if current_leftmost[0] is None or current_leftmost[1] < level:
                current_leftmost = (node, level)
            # push children into queue
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return current_leftmost[0].val