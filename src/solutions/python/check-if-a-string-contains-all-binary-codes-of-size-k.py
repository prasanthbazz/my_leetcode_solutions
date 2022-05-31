'''
#1461
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k
'''
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        hashset = set()
        hashval = int(s[:k], 2)
        hashset.add(hashval)
        for i in range(k, n):
            hashval -= (int(s[i-k])<<(k-1))
            hashval <<= 1
            hashval += int(s[i])
            hashset.add(hashval)
        return len(hashset) == 1<<k