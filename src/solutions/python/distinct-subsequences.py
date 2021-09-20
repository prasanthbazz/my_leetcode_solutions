'''
#115
https://leetcode.com/problems/distinct-subsequences/
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [0 for i in range(len(s))]
        so_far = 1
        for i in range(len(t)):
            for j in range(len(s)):
                temp = dp[j]
                if t[i] == s[j]:
                    dp[j] = so_far
                else:
                    dp[j] = 0
                so_far += temp
            so_far = 0
        return sum(dp)