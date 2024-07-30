class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)==0):return True
        if(len(s)>len(t)):return False
        i=0
        for j in t:
            if s[i]==j:
                i+=1
                if(i>len(s)-1):break
        if(i==len(s)):
            return True
        else:
            return False