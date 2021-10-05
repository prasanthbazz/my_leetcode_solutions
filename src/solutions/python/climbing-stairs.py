'''
#70
https://leetcode.com/problems/climbing-stairs/submissions/
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        oneStepBefore = 1
        twoStepBefore = 0
        for i in range(n):
            temp = twoStepBefore
            twoStepBefore = oneStepBefore
            oneStepBefore += temp
        return oneStepBefore