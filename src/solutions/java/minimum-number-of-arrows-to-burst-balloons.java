/*
#452
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
*/
class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, new Comparator<int[]>(){
            public int compare(int[] p1, int[] p2){
                return (p1[0] < p2[0])?-1:1;
            }});
        int res = 1, second = points[0][1];
        for(int i = 1; i < points.length; i++){
            if(points[i][0] <= second){
                second = Math.min(second, points[i][1]);
            }
            else{
                res ++;
                second = points[i][1];
            }
        }
        return res;
    }
}