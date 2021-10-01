'''
#698
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        seen = [False] * len(nums)
        return self.canMakeSubset(nums, 0, 0, k, nums_sum//k, seen)
    
    def canMakeSubset(self, nums, curr_ind, soFarSum, remainingSubsets, subsetSum, seen):
        if soFarSum == subsetSum:
            soFarSum = 0
            curr_ind = 0
            remainingSubsets -= 1
        # early return since anyway the last subset can be formed
        if remainingSubsets == 1:
            return True
        for i in range(curr_ind, len(nums)):
            if seen[i] or nums[i] + soFarSum > subsetSum:
                continue
            seen[i] = True
            if self.canMakeSubset(nums, i+1, soFarSum + nums[i], remainingSubsets, subsetSum, seen):
                return True
            seen[i] = False
        return False