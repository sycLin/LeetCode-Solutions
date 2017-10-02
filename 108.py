# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        midValue = nums[len(nums) / 2]
        root = TreeNode(midValue)
        leftSubTree = self.sortedArrayToBST(nums[:len(nums) / 2])
        rightSubTree = self.sortedArrayToBST(nums[len(nums) / 2 + 1:])
        root.left = leftSubTree
        root.right = rightSubTree
        return root
