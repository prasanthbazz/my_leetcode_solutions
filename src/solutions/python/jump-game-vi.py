'''
#1696
https://leetcode.com/problems/jump-game-vi
'''
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        T.C - O(N)
        S.C - O(N)
        '''
        queue = collections.deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            if i - queue[0][1] > k:
                queue.popleft()
            nxt = queue[0][0] + nums[i]
            while queue and queue[-1][0] <= nxt:
                queue.pop()
            queue.append((nxt,i))
        return queue[-1][0]