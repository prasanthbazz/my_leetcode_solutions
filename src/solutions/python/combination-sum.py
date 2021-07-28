'''
#39
https://leetcode.com/problems/combination-sum/
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        #dfs breaks early
        candidates.sort(reverse = True)
        self.dfs(candidates, 0, 0, [], res, target)
        return res

    def dfs(self, nums, so_far, prev, arr, res, target):
        if so_far > target:
            return
        if so_far == target:
            res.append(arr)
        
        for i in range(prev, len(nums)):
            self.dfs(nums, so_far + nums[i], i, arr + [nums[i]], res, target)