'''
#113
https://leetcode.com/problems/path-sum-ii/
'''
# Definition for a binary tree node.
# class TreeNode(object)
#     def __init__(self, val=0, left=None, right=None)
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object)
    def pathSum(self, root, targetSum)
        
        type root TreeNode
        type targetSum int
        rtype List[List[int]]
        
        self.targetSum = targetSum
        res = []
        self.calculatePathSum(root, [], 0, res)
        return res
    
    def calculatePathSum(self, node, path, so_far_sum, res)
        if not node
            return
        so_far_sum += node.val
        temp = path + [node.val]
        if not node.left and not node.right
            if so_far_sum == self.targetSum
                res.append(temp)
            return
        self.calculatePathSum(node.left, temp, so_far_sum, res)
        self.calculatePathSum(node.right, temp, so_far_sum, res)