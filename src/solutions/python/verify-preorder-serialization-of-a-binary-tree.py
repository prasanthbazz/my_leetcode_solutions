'''
#331
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
'''
class Solution(object)
    def isValidSerialization(self, preorder)
        
        type preorder str
        rtype bool
        
        lst = preorder.split(',')
        stack = []
        if lst[0] != '#'
            stack.append(0)
        for i in range(1, len(lst))
            if not stack
                return False
            if stack[-1] == 1
                stack.pop(-1)
            else
                stack[-1] = 1
            if lst[i] != '#'
                stack.append(0)
        return not stack