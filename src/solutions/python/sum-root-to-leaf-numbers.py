'''
#129
https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.dfs(root, res, 0)
        return res[0]
    
    def dfs(self, node, res, so_far):
        if not node:
            return
        so_far *= 10
        so_far += node.val
        if not node.left and not node.right:
            res[0] += so_far
            return
        self.dfs(node.left, res, so_far)
        self.dfs(node.right, res, so_far)