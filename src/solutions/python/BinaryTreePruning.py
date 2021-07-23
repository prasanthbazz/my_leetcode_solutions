'''
#814
https://leetcode.com/problems/binary-tree-pruning/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode()
        dummy.left = root
        self.isSubtreeNeeded(dummy)
        return dummy.left
    
    def isSubtreeNeeded(self, node):
        if not node:
            return False
        l = self.isSubtreeNeeded(node.left)
        if not l:
            node.left = None
        r = self.isSubtreeNeeded(node.right)
        if not r:
            node.right = None
        return l or r or node.val == 1