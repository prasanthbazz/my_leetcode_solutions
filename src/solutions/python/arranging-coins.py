'''
#441
https://leetcode.com/problems/arranging-coins/
'''
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 1
        while(n >= cnt):
            n -= cnt
            cnt += 1
        return cnt-1