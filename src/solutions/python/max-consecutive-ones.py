'''
#485
https://leetcode.com/problems/max-consecutive-ones/
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        res = 0
        for i in nums:
            if i == 1:
                cnt += 1
            else:
                res = max(cnt, res)
                cnt = 0
        return max(cnt, res)