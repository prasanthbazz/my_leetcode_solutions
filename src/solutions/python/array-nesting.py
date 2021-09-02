'''
#565
https://leetcode.com/problems/array-nesting/
'''
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [0]*len(nums)
        maxi = 0
        for i in range(len(nums)):
            cnt = 0
            while(seen[i] == 0):
                seen[i] = 1
                i = nums[i]
                cnt += 1
            maxi = max(cnt, maxi)
        return maxi