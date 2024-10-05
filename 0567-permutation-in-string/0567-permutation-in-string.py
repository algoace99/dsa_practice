class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1)==1 and s1 in s2) or s1 == s2:
            return True
        s1_count = Counter(s1)
        for i in range(0,len(s2)-len(s1)+1):
            s2_count = Counter(s2[i:i+len(s1)])
            if s1_count == s2_count:
                return True
        return False