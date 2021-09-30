'''
#725
https://leetcode.com/problems/split-linked-list-in-parts/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        tot_len = 0
        node = head
        while(node):
            node = node.next
            tot_len += 1
        res = []
        curr_head = head
        while(k > 0):
            group_len = (tot_len + (k-1))//k
            res.append(curr_head)
            temp = curr_head
            prev = None
            for j in range(group_len):
                prev = temp
                temp = temp.next
            if prev:
                prev.next = None
            curr_head = temp
            tot_len -= group_len
            k -= 1
        return res