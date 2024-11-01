class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        se = set()
        for i in range(len(rev)-1):
            se.add(rev[i:i+2])
        for i in range(len(s)-1):
            if s[i:i+2] in se:
                return True
        return False