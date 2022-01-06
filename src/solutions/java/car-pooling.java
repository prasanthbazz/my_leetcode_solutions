/*
#1094
https://leetcode.com/problems/car-pooling/
*/
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        Arrays.sort(trips, new Comparator<int[]>(){
            public int compare(int[] t1, int[] t2)
            {
                return t1[1] - t2[1];
            }
        });
        Queue<int[]> dropLocationQueue = new PriorityQueue<int[]>(new Comparator<int[]>(){
            public int compare(int[] t1, int[] t2)
            {
                return t1[2] - t2[2];
            }
        });
        int curr = 0;
        for(int [] trip : trips)
        {
            while(!dropLocationQueue.isEmpty() && dropLocationQueue.peek()[2] <= trip[1])
            {
                curr -= dropLocationQueue.remove()[0];
            }
            curr += trip[0];
            if(curr > capacity)
            {
                return false;
            }
            dropLocationQueue.add(trip);
        }
        return true;
    }
}