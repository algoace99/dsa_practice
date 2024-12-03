class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j = 0
        for i in range(len(spaces)):
            ans += s[j:spaces[i]]
            ans += " "
            j = spaces[i]
        ans += s[j:]
        return ans