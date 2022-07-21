class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findMaxRobbedAmountWithingRange(l, r):
            notRobbingPrev = 0
            robbingPrev = 0
            for i in range(l, r+1):
                robbingCurr = notRobbingPrev + nums[i]
                notRobbingPrev = max(robbingPrev, notRobbingPrev)
                robbingPrev = robbingCurr
            return max(robbingPrev, notRobbingPrev)
        if len(nums) == 1:
            return nums[0]
        
        return max(findMaxRobbedAmountWithingRange(0, len(nums)-2), findMaxRobbedAmountWithingRange(1, len(nums)-1))