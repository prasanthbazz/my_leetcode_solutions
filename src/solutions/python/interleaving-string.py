'''
#97
https://leetcode.com/problems/interleaving-string/
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        dp[0][0] = True
        for j in range(len(s2)):
            dp[0][j+1] = dp[0][j] and s2[j] == s3[j]
        for i in range(len(s1)):
            dp[i+1][0] = dp[i][0] and s1[i] == s3[i]
            for j in range(len(s2)):
                dp[i+1][j+1] = (dp[i][j+1] and s1[i] == s3[i+j+1]) or (dp[i+1][j] and s2[j] == s3[i+j+1])
        return dp[-1][-1]