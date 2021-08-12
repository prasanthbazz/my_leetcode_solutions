'''
#926
https://leetcode.com/problems/flip-string-to-monotone-increasing/
'''
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_0, prev_1 = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                prev_1 = min(prev_0, prev_1)
                prev_0 = prev_0 + 1
            if s[i] == '0':
                prev_1 = min(prev_1, prev_0) + 1
        return min(prev_1, prev_0)