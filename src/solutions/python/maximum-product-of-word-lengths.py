'''
#318
https://leetcode.com/problems/maximum-product-of-word-lengths/
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordRepresentation = []
        for w in words:
            temp = 0
            for i in w:
                temp |= (1 << (ord(i) - ord('a')))
            wordRepresentation.append(temp)
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if wordRepresentation[i] & wordRepresentation[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res