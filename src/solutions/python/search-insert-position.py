'''
#35
https://leetcode.com/problems/search-insert-position
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)
        while(l < r):
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid+1
        return l