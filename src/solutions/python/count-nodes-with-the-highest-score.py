'''
#2049
https://leetcode.com/problems/count-nodes-with-the-highest-score/
'''
class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        self.n = len(parents)
        children = [[] for i in range(self.n)]
        self.maxi = -1
        self.res = 0
        for i in range(1, len(parents)):
            children[parents[i]].append(i)
        self.findScore(children, 0)
        return self.res
        
    def findScore(self, children, node):
        cnt = 0
        product = 1
        for c in children[node]:
            cur = self.findScore(children, c)
            cnt += cur
            product *= cur
        product *= max(1, self.n - cnt - 1)
        if product > self.maxi:
            self.maxi = product
            self.res = 1
        elif product == self.maxi:
            self.res += 1
        return cnt + 1