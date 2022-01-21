'''
#134
https://leetcode.com/problems/gas-station/
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        start = 0
        fuelLeft = 0
        for i in range(0, len(gas)):
            fuelLeft += gas[i] - cost[i]
            if fuelLeft < 0:
                start = i+1
                fuelLeft = 0
        return start