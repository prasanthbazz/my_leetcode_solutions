/*
#421
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
*/
class Solution {
    public int findMaximumXOR(int[] nums) {
        TrieNode head = new TrieNode();
        //populting Trie
        for(int num : nums){
            int mask = 1 << 30;
            TrieNode node = head;
            for(int i = 0; i < 31; i++){
                if((num & mask) != 0){
                    if(node.oneChild == null)
                        node.oneChild = new TrieNode();
                    node = node.oneChild;
                }    
                else{
                    if(node.zeroChild == null)
                        node.zeroChild = new TrieNode();
                    node = node.zeroChild;
                }
                mask >>= 1;
            }
        }
        int maxXor = 0;
        for(int num : nums){
            int currBestXor = 0;
            TrieNode node = head;
            int mask = 1 << 30;
            for(int i = 0; i < 31; i++){
                currBestXor <<= 1;
                if((num & mask) == 0){
                    if(node.oneChild != null){
                        node = node.oneChild;
                        currBestXor |= 1;
                    }
                    else{
                        node = node.zeroChild;
                    }
                }
                else{
                    if(node.zeroChild != null){
                        node = node.zeroChild;
                        currBestXor |= 1;
                    }
                    else{
                        node = node.oneChild;
                    }
                }
                mask >>= 1;
            }
            maxXor = Math.max(maxXor, currBestXor);
        }
        return maxXor;
    }
}

class TrieNode {
    public TrieNode oneChild;
    public TrieNode zeroChild;
    
    public TrieNode() {
        oneChild = null;
        zeroChild = null;
    }
}