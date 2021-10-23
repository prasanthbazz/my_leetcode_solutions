'''
#151
https://leetcode.com/problems/reverse-words-in-a-string/
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = ''
        res = ""
        for i in s[::-1]:
            if i == ' ':
                if temp:
                    res += " "
                    res += temp[::-1]
                temp = ''
            else:
                temp += i
        if temp:
            res += " " + temp[::-1]
        return res[1:]