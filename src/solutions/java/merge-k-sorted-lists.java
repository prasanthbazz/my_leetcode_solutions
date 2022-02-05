/*
#22
https://leetcode.com/problems/merge-k-sorted-lists/
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(new Comparator<ListNode>(){
            public int compare(ListNode l1, ListNode l2){
                return l1.val - l2.val;
            }
        });
        for(ListNode l: lists){
            if(l != null) pq.add(l);
        }
        ListNode res = new ListNode();
        ListNode dummy = res;
        while(!pq.isEmpty()){
            ListNode curr = pq.poll();
            if(curr.next != null) pq.add(curr.next);
            curr.next = null;
            dummy.next = curr;
            dummy = dummy.next;
        }
        return res.next;
    }
}