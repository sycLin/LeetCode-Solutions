# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        #
        # perform BFS
        #
        ret = []
        queue = []
        queue.append((root, 0))
        while len(queue) > 0:
            # dequeue and enqueue children
            node, level = queue.pop(0)
            values = [node.val]
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            # dequeue all same-level nodes
            # to calculate average
            while len(queue) > 0 and queue[0][1] == level:
                node, level = queue.pop(0)
                values.append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
            ret.append(sum(values) * 1.0 / len(values))
        return ret
            
        