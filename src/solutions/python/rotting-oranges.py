'''
#994
https://leetcode.com/problems/rotting-oranges
'''
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        curr_rotten = collections.deque([])
        n, m = len(grid), len(grid[0])
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    curr_rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        neighbours = [[1,0], [0,1], [-1,0], [0,-1]]
        new_rotten = []
        res = 0
        if fresh == 0:
            return 0
        while(curr_rotten):
            for ind in range(0, len(curr_rotten)):
                i, j = curr_rotten[ind]
                for d in neighbours:
                    nxt_i = i + d[0]
                    nxt_j = j + d[1]
                    if nxt_i >= 0 and nxt_j >= 0 and nxt_i < n and nxt_j < m and grid[nxt_i][nxt_j] == 1:
                        grid[nxt_i][nxt_j] = 2
                        new_rotten.append([nxt_i, nxt_j])
                        fresh -= 1
                        if fresh == 0:
                            return res + 1
            res += 1
            curr_rotten = new_rotten
            new_rotten = []
        return -1