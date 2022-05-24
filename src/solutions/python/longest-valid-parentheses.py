'''
#32
https://leetcode.com/problems/longest-valid-parentheses/
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        st = []
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                if st and s[st[-1]] == '(':
                    st.pop(-1)
                else:
                    st.append(i)
        res = 0
        prev = n
        for i in range(len(st)-1, -1, -1):
            res = max(res, prev - st[i] - 1)
            prev = st[i]
        return max(res, prev)