class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            ind = abs(i)
            nums[ind-1] = -abs(nums[ind-1])
            #print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res