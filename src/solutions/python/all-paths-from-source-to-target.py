'''
#797
https://leetcode.com/problems/all-paths-from-source-to-target/
'''
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(graph, 0, [0])
        return self.res
    def dfs(self, graph, curr, so_far):
        if curr == len(graph)-1:
            self.res.append(so_far[:])
        for i in graph[curr]:
            self.dfs(graph, i, so_far+[i])
        return