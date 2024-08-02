class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s=Counter(s)
        t=Counter(t)
        if s==t:
            return True
        return False