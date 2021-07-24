'''
#1936
https://leetcode.com/problems/add-minimum-number-of-rungs/
'''
class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        curr = 0
        i = 0
        res = 0
        while(i < len(rungs)):
            nxt = rungs[i]
            if nxt - curr > dist:
                gap = nxt - curr
                count = (gap + dist - 1)//dist
                res += count-1
                curr += dist * (count - 1)
            else:
                curr = nxt
                i += 1
        return res