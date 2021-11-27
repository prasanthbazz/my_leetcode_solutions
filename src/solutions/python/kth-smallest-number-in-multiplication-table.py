'''
#668
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table
'''
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        l, r = 1, m*n
        while(l < r):
            mid = (l + r)//2
            cnt = self.noOfElementsLessThanP(m, n, mid)
            if cnt >= k:
                r = mid
            else:
                l = mid+1
        return l
    
    def noOfElementsLessThanP(self, m, n, P):
        cnt = 0
        for i in range(1, m+1):
            cnt += min(P//i, n)
        return cnt