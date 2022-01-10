/*
#67
https://leetcode.com/problems/add-binary/
*/
class Solution {
    public String addBinary(String a, String b) {
        char carry = '0';
        int m = a.length();
        int n = b.length();
        StringBuilder sb = new StringBuilder();
        int i;
        for(i = 0; i < m && i < n; i++)
        {
            char
                tempres[] = addBits(a.charAt(m-i-1), b.charAt(n-i-1));
            char
                res[] = addBits(tempres[0], carry);
            sb.append(res[0]);
            if(tempres[1] == '1' || res[1] == '1')
                carry = '1';
            else
                carry = '0';
        }
        for(int j = i; j < m; j++)
        {
            char
                tempres[] = addBits(a.charAt(m-j-1), carry);
            sb.append(tempres[0]);
            carry = tempres[1];
        }
        for(int j = i; j < n; j++)
        {
            char
                tempres[] = addBits(b.charAt(n-j-1), carry);
            sb.append(tempres[0]);
            carry = tempres[1];
        }
        if(carry == '1')
            sb.append('1');
        return sb.reverse().toString();
    }
    private char[] addBits(char a, char b)
    {
        if(a == '0' && b == '0')
        {
            return new char[] {'0','0'};
        }
        else if(a == '1' && b == '0' || a == '0' && b == '1')
        {
            return new char[] {'1','0'};
        }
        else
        {
            return new char[] {'0','1'};
        }
    }
}