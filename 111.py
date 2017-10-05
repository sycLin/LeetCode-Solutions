# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # solution with BFS
        if not root:
            return 0
        queue = []
        currentLayer = 1 # root is in Layer-1 (my definition)
        queue.append(root)
        while True:
            tmpQueue = []
            while len(queue) > 0:
                node = queue.pop()
                if node.left == None and node.right == None:
                    return currentLayer
                if node.left:
                    tmpQueue.append(node.left)
                if node.right:
                    tmpQueue.append(node.right)
            queue = tmpQueue
            currentLayer += 1
        return currentLayer # not necessary
