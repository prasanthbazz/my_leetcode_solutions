/*
#1010
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
*/
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        int res = 0;
        for(int i: time)
        {
            res += hm.getOrDefault((600-i)%60, 0);
            hm.put(i%60, hm.getOrDefault(i%60, 0)+1);
        }
        return res;
    }
}