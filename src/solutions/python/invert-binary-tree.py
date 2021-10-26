'''
#226
https://leetcode.com/problems/invert-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        tempNode = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(tempNode)
        return root