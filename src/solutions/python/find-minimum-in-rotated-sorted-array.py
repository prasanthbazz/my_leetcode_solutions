'''
#153
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        l, r = 0, len(nums)-1
        while(l < r):
            mid = (l+r)//2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        return a[l]