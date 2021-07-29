'''
#542
https://leetcode.com/problems/01-matrix/
'''
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(mat), len(mat[0])
        dist = [[-1 for j in range(n)] for i in range(m)]
        queue = collections.deque([])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        adjacents = [(1,0), (0,1), (-1,0), (0,-1)]
        curr_dist = 0
        while queue:
            curr_dist += 1
            for k in range(len(queue)):
                i, j = queue.popleft()
                for adj in adjacents:
                    nxt_i = i + adj[0]
                    nxt_j = j + adj[1]
                    if (0 <= nxt_i <= m-1) and (0 <= nxt_j <= n-1) and dist[nxt_i][nxt_j] == -1:
                        dist[nxt_i][nxt_j] = curr_dist
                        queue.append((nxt_i, nxt_j))
        return dist