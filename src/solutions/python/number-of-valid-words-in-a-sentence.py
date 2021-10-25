'''
#2047
https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
'''
class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        word_lst = sentence.split(" ")
        res = 0
        for w in word_lst:
            if w == '':
                continue
            isWord = True
            hyphFound = False
            for l in range(0, len(w)):
                if w[l].isdigit():
                    isWord = False
                    break
                elif (w[l] == '.' or w[l] == ',' or w[l] == '!') and l != len(w)-1:
                    isWord = False
                    break
                elif w[l] == '-':
                    if (l == 0 or l == len(w)-1 or not w[l-1].isalpha() or not w[l+1].isalpha() or hyphFound):
                        isWord = False
                        break
                    else:
                        hyphFound = True
            if isWord:
                res += 1
        return res