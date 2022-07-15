class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        seen = [[False for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.connectIslandAndCalculateArea(grid, i, j, seen))
        return res
    
    def connectIslandAndCalculateArea(self, grid, i, j, seen):
        if i == len(grid) or i < 0 or j == len(grid[0]) or j < 0 or grid[i][j] != 1 or seen[i][j]:
            return 0
        seen[i][j] = True
        return 1 + self.connectIslandAndCalculateArea(grid, i, j+1, seen) + self.connectIslandAndCalculateArea(grid, i, j-1, seen) + self.connectIslandAndCalculateArea(grid, i+1, j, seen) + self.connectIslandAndCalculateArea(grid, i-1, j, seen)