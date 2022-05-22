'''
#647
https://leetcode.com/problems/palindromic-substrings/
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [False for i in range(n)]
        
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, i-1, -1):
                dp[j] = s[i] == s[j] and (j-i+1 < 3  or dp[j-1])
                if dp[j]:
                    res += 1
        return res