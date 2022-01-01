/*
#312
https://leetcode.com/problems/burst-balloons/
*/
class Solution {
    int[][] dp = new int[501][501];
    public int maxCoins(int[] nums) {
        for(int[] temp:dp)
            Arrays.fill(temp, -1);
        return maxCoinsInRange(0, nums.length-1, nums);
    }
    
    private int maxCoinsInRange(int start, int end, int[]nums)
    {   
        int maxCoins = 0;
        int prev, nxt;
        if(start <= end)
        {
            if(dp[start][end] !=-1)
                return dp[start][end];
            if(start==0)
                prev = 1;
            else
                prev = nums[start-1];
            if(end == nums.length-1)
                nxt = 1;
            else
                nxt = nums[end+1];
            for(int i = start; i <= end; i++)
            {
                int currProduct = nums[i] * prev * nxt;
                maxCoins = Math.max(maxCoins, currProduct + maxCoinsInRange(start, i-1, nums) + maxCoinsInRange(i+1, end, nums));
            }
            dp[start][end] = maxCoins;
            return maxCoins;
        }
        else
        {
            return 0;
        }
    }
}