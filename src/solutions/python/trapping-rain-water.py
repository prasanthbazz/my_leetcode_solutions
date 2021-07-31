'''
#42
https://leetcode.com/problems/trapping-rain-water/
'''
'''
To-Do : try solving with constant space
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for r in range(len(height)):
            while stack and height[stack[-1]] <= height[r]:
                depth = height[stack.pop(-1)]
                if stack:
                    l = stack[-1]
                    res += (min(height[r], height[l]) - depth) * (r - l - 1)
            stack.append(r)
        return res