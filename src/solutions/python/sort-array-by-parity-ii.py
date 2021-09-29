'''
#922
https://leetcode.com/problems/sort-array-by-parity-ii/
'''
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ev_pointer = 0
        od_pointer = len(nums)-1
        
        while ev_pointer < len(nums) and od_pointer >= 0:
            if nums[ev_pointer] % 2 == 0:
                ev_pointer += 2
            elif nums[od_pointer] % 2:
                od_pointer -= 2
            else:
                nums[ev_pointer], nums[od_pointer] =  nums[od_pointer], nums[ev_pointer]
                ev_pointer += 2
                od_pointer -= 2
        return nums