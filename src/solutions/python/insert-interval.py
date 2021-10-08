'''
#57
https://leetcode.com/problems/insert-interval/
'''
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        start, end, res = newInterval[0], newInterval[1], []
        i = 0
        while(i < len(intervals) and start > intervals[i][1]):
            res.append(intervals[i])
            i += 1
        while(i < len(intervals) and intervals[i][0] <= end):
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])
        
        while(i < len(intervals)):
            res.append(intervals[i])
            i += 1
        return res