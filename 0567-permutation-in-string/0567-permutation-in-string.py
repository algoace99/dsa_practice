class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        l=0
        r=len(s1)
        d1=Counter(s1)
        while r<=len(s2):
            if Counter(s2[l:r]) == d1:
                return True
            r+=1
            l+=1
        return False