class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        if len(s)==1:
            return s
        if s==s[:][::-1]:
            return s
        start = 0
        end = len(s)-1
        while start <= end:
            if s[:end]==s[:end][::-1]:
                return s[end:][::-1]+s
            else:
                end -= 1