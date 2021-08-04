'''
#90
https://leetcode.com/problems/subsets-ii/
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        res = []
        self.formSubsets(dic.items(), 0, [], res)
        return res
        
    def formSubsets(self, lst, ind, curr, res):
        if ind == len(lst):
            res.append(curr)
            return
        temp = []
        for i in range(lst[ind][1] + 1):
            self.formSubsets(lst, ind + 1, curr + temp, res)
            temp.append(lst[ind][0])