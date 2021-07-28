'''
#76
https://leetcode.com/problems/minimum-window-substring/
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in t:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        remaining = len(t)
        res_index = -1
        res_len = len(s) + 1
        j = 0
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] -= 1
                if dic[s[i]] >= 0:
                    remaining -= 1
                    #print(remaining)
            while(j <= i and (s[j] not in dic or dic[s[j]] < 0)):
                if s[j] in dic:
                    dic[s[j]] += 1
                j += 1
            if remaining == 0:
                if i - j + 1 < res_len:
                    res_len = i - j + 1
                    res_index = j
        #print(res_len)
        if res_index == -1:
            return ""
        return s[res_index : res_index+res_len]