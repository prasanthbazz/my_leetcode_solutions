'''
#1629
https://leetcode.com/problems/slowest-key/
'''
class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        res = keysPressed[0]
        maxi = releaseTimes[0]
        n = len(keysPressed)
        for i in range(1, n):
            time = releaseTimes[i] - releaseTimes[i-1]
            if time > maxi or (time == maxi and keysPressed[i] > res):
                res = keysPressed[i]
                maxi = time
        return res