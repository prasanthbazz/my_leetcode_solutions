/*
#8
https://leetcode.com/problems/string-to-integer-atoi/
*/
class Solution {
    public int myAtoi(String s) {
        int i = 0, n = s.length(), res = 0;
        boolean isNegative = false;
        while(i < n && s.charAt(i) == ' ') i++;
        if(i < n && (s.charAt(i) == '-' || s.charAt(i) == '+')) isNegative = s.charAt(i++) == '-';
        while( i < n && s.charAt(i) <= '9' && s.charAt(i) >= '0'){
            if(res > Integer.MAX_VALUE/10 || res == Integer.MAX_VALUE/10 && s.charAt(i) > '7')
                return isNegative?Integer.MIN_VALUE:Integer.MAX_VALUE;
            res *= 10;
            res += s.charAt(i) - '0';
            i++;
        }
        return res * (isNegative?-1:1);
    }
}