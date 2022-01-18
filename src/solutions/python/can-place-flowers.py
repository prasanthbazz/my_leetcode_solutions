'''
#605
https://leetcode.com/problems/can-place-flowers/
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        validPlotsCnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                validPlotsCnt += 1
                flowerbed[i] = 1
        return validPlotsCnt >= n