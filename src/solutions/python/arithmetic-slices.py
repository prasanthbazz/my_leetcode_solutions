'''
#413
https://leetcode.com/problems/arithmetic-slices/
'''
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        start = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                res += (i - start - 1)
            else:
                start = i - 1
        return res