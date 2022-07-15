class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if sum(matchsticks) % 4 != 0:
            return False
        return self.dfs(matchsticks, 0, [0,0,0], matchsticks//4)
        
    def dfs(self, matchsticks, currInd, lengthOfSides, k):
        if currInd == len(matchsticks):
            return lengthOfSides[0] == lengthOfSides[1] == lengthOfSides[2] == k
        res = False
        for i in range(3):
            if matchsticks[currInd] + lengthOfSides[i] <= k:
                lengthOfSides[i] += matchsticks[currInd]
                if self.dfs(matchsticks, currInd+1, lengthOfSides, k):
                    return True
                lengthOfSides[i] -= matchsticks[currInd]
        return self.dfs(matchsticks, currInd+1, lengthOfSides, k)