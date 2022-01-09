/*
#1041
https://leetcode.com/problems/robot-bounded-in-circle/
*/
class Solution {
    public boolean isRobotBounded(String instructions) {
        int directions[][] = {{0,1},{1,0},{0,-1},{-1,0}};
        int []curr = {0,0,0};
        for(int i = 0; i < instructions.length(); i++)
        {
            if(instructions.charAt(i) == 'L')
                curr[2] = (curr[2] + 3)%4;
            else if(instructions.charAt(i) == 'R')
                curr[2] = (curr[2] + 1)%4;
            else
            {
                curr[0] += directions[curr[2]][0];
                curr[1] += directions[curr[2]][1];
            }
        }
        
        if(curr[2] != 0 || curr[0] == 0 && curr[1] == 0)
            return true;
        return false;
    }
}