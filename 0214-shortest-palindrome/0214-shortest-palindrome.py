class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        if len(s)==1:
            return s

        rev_s = s[::-1]
        if s==rev_s:
            return s
        end = len(s) - 1 
        while end >= 0:
            if s[:end] == rev_s[len(s) - end:]:
                return rev_s[:len(s) - end] + s
            end -= 1
        return "" 