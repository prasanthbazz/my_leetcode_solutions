'''
#108
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.FormTreeNode(nums, 0, len(nums))
    
    def FormTreeNode(self, nums, l, r):
        if l >= r:
            return None
        mid = (l+r)//2
        node =  TreeNode(nums[mid])
        node.left = self.FormTreeNode(nums, l, mid)
        node.right = self.FormTreeNode(nums, mid+1, r)
        return node