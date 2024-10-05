class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = {}
        for i in range(0,len(s2)-len(s1)+1):
            s2_count = Counter(s2[i:i+len(s1)])
            if s1_count == s2_count:
                return True
        return False