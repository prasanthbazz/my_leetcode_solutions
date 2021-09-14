'''
#1189
https://leetcode.com/problems/maximum-number-of-balloons/
'''
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for i in text:
            dic[i] += 1
        
        return min(dic['b'], dic['a'], dic['l']//2, dic['o']//2, dic['n'])