/*
#849
https://leetcode.com/problems/maximize-distance-to-closest-person/
*/
class Solution {
    public int maxDistToClosest(int[] seats) {
        int n = seats.length;
        int last = -1;
        int res = 0;
        for(int i = 0; i < n; i++){
            if(seats[i] == 1){
                res = Math.max(res, (last == -1)?i:(i-last)/2);
                last = i;
            }
        }
        return Math.max(res, n-1-last);
    }
}