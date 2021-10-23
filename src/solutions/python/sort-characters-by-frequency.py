class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq_dic = collections.defaultdict(int)
        for i in s:
            freq_dic[i] += 1
        return ''.join(sorted(s, key = lambda x:(freq_dic[x],x), reverse = True))