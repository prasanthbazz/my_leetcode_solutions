'''
#474
https://leetcode.com/problems/ones-and-zeroes/
'''
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def calculate(st):
            z = 0
            o = 0
            for j in st:
                if j == '0':
                    z += 1
                else:
                    o += 1
            return (z, o)
        
        l = len(strs)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(l-1, -1, -1):
            zeroesCount, onesCount = calculate(strs[i])
            for j in range(m-zeroesCount+1):
                for k in range(n-onesCount+1):
                    dp[j][k] = max(dp[j][k], 1 + dp[j + zeroesCount][k + onesCount])
        return dp[0][0]