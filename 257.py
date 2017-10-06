# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        if not root:
            return []
        queue = []
        queue.append((root, "%d" % root.val))
        while len(queue) > 0:
            n, p = queue.pop(0)
            if n.left == None and n.right == None:
                ret.append(p)
            if n.left:
                queue.append((n.left, "%s->%d" % (p, n.left.val)))
            if n.right:
                queue.append((n.right, "%s->%d" % (p, n.right.val)))
        return ret
        
