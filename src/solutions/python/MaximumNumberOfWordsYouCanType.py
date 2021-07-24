'''
#1935
https://leetcode.com/problems/maximum-number-of-words-you-can-type/
'''
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split(' ')
        brokenLettersSet = set()
        for i in brokenLetters:
            brokenLettersSet.add(i)
        res = 0
        for w in words:
            canTyped = 1
            for l in w:
                if l in brokenLettersSet:
                    canTyped = 0
                    break
            res += canTyped
        return res