'''
#415
https://leetcode.com/problems/add-strings/
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        while(i >=0 and j >=0):
            temp = int(num1[i]) + int(num2[j]) + carry
            if temp >= 10:
                carry = 1
            else:
                carry = 0
            res = str(temp%10) + res
            i -= 1
            j -= 1
        while(i >= 0):
            temp = int(num1[i]) + carry
            if temp >= 10:
                carry = 1
            else:
                carry = 0
            res  = str(temp%10) + res
            i -= 1
        while j >= 0:
            temp = int(num2[j]) + carry
            if temp >= 10:
                carry = 1
            else:
                carry = 0
            res  = str(temp%10) + res
            j -= 1
        if carry:
            res = '1' + res
        return res