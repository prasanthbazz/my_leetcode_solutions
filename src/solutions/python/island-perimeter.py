'''
#463
https://leetcode.com/problems/island-perimeter/
'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    for d in directions:
                        di = i + d[0]
                        dj = j + d[1]
                        if di >= len(grid) or di < 0 or dj >= len(grid[0]) or dj < 0 or grid[di][dj] == 0:
                            res += 1
        return res