'''
#494
https://leetcode.com/problems/target-sum/
'''

#solved using dfs + memo. To-Do: try using DP
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.dfs(0, nums, 0, target, {})

    def dfs(self, so_far, nums, curr, target, memo):
        if curr == len(nums):
            if so_far == target:
                return 1
            return 0
        memo_str = str(curr)+'.'+str(so_far)
        if memo_str in memo:
            return memo[memo_str]
        res = 0
        res += self.dfs(so_far+nums[curr], nums, curr+1, target, memo)
        res += self.dfs(so_far-nums[curr], nums, curr+1, target, memo)
        memo[memo_str] = res
        return res