'''
#279
https://leetcode.com/problems/perfect-squares/
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while(j*j <= i):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j+=1
        return dp[n]