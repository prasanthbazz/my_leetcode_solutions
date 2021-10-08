'''
#684
https://leetcode.com/problems/redundant-connection/
'''
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        edges_map = [[] for i in range(n+1)]
        for i in (edges):
            if self.dfs(i[1], i[0], i[1], edges_map):
                return i
            else:
                edges_map[i[0]].append(i[1])
                edges_map[i[1]].append(i[0])
    
    def dfs(self, parent, node, pre_node, edges_map):
        if parent == node:
            return True
        for i in edges_map[node]:
            if i == pre_node:
                continue
            if self.dfs(parent, i, node, edges_map):
                return True
        return False