class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for l in range(len(s)-2):
            if len(set(s[l:l+3])) == 3:
                count += 1
        return count