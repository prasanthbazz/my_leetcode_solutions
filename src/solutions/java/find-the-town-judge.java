/*
#997
https://leetcode.com/problems/find-the-town-judge
*/
class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] trustCount = new int[n+1];
        
        for(int i = 0; i < trust.length; i++)
        {
            trustCount[trust[i][0]] -= 1;
            trustCount[trust[i][1]] += 1;
        }

        for(int i = 1; i <= n; i++)
        {
            if(trustCount[i] == n-1)
                return i;
        }
        return -1;
    }
}