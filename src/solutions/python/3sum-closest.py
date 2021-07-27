'''
#16
https://leetcode.com/problems/3sum-closest/
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        mini = float('inf')
        res = -1
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            sum1 = nums[i]
            while(l < r):
                sum1 = nums[i] + nums[l] + nums[r]
                if sum1 < target:
                    l += 1
                elif sum1 > target:
                    r -= 1
                else:
                    return target
                if abs(target - sum1) < mini:
                    mini = abs(target - sum1)
                    res = sum1
        return res