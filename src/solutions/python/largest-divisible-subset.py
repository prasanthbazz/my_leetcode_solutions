'''
#368
https://leetcode.com/problems/largest-divisible-subset/
'''
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp = [[1, -1] for i in nums] #dp[i][0] stores the maximum length of subset beginning with nums[i] and dp[i][1] stores the index of next element to i in the largest subset
        
        n = len(dp)
        maxi = 0
        idx = n-1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[j] % nums[i] == 0 and dp[j][0] >= dp[i][0]:
                    dp[i][0] = 1 + dp[j][0]
                    dp[i][1] = j
            if dp[i][0] > maxi:
                maxi = dp[i][0]
                idx = i
        res = []
        while(idx != -1):
            res.append(nums[idx])
            idx = dp[idx][1]
        return res