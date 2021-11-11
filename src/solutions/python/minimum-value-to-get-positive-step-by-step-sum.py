'''
#1413
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum
'''
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        so_far = 0
        for i in range(len(nums)):
            so_far += nums[i]
            maxi = max(maxi, -so_far)
        return maxi+1