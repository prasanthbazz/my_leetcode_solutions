'''
#1239
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        return self.makeCombinations(arr, 0, 0, 0)
    def makeCombinations(self, arr, curr, len_so_far, mask):
        if curr == len(arr):
            return len_so_far
        isUnique = True
        temp_mask = mask
        for i in arr[curr]:
            #bit masking
            ind = ord(i) - ord('a')
            if temp_mask & 1<<ind != 0:
                isUnique = False
                break
            temp_mask |= 1<<ind
        y, n = 0, 0
        if isUnique:
            y = self.makeCombinations(arr, curr+1, len_so_far + len(arr[curr]), temp_mask)
        n = self.makeCombinations(arr, curr+1, len_so_far, mask)
        
        return max(y, n)