'''
#739
https://leetcode.com/problems/daily-temperatures/
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temperatures)
        
        for i in range(len(temperatures)-2, -1, -1):
            j = i+1
            while(temperatures[j] <= temperatures[i]):
                if res[j] == 0:
                    j = i
                    break
                j += res[j]
            res[i] = j - i
        return res