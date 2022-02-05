/*
#525
https://leetcode.com/problems/contiguous-array
*/
class Solution {
    public int findMaxLength(int[] nums) {
        int res = 0;
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        
        hm.put(0, -1);
        int curr = 0;

        for(int i = 0; i < nums.length; i++){
            curr += (nums[i] == 0)?-1:1;
            if(hm.containsKey(curr)){
                res = Math.max(res, i-hm.get(curr));
            }
            else hm.put(curr, i);
        }
        
        return res;
    }
}