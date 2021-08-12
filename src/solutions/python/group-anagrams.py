'''
#49
https://leetcode.com/problems/group-anagrams/
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        Time Complexity
        O(n*l*log(l)) , where l - average length of a word in strs
        Space Complexity
        O(n)
        """
        letters_dict = collections.defaultdict(list)

        for wrd in strs:
            letters_dict[''.join(sorted(wrd))].append(wrd)
        res = []
        for wrd in letters_dict:
            res.append(letters_dict[wrd])
        return res