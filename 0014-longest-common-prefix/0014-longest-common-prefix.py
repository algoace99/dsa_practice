class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        min_length = min(len(i) for i in strs)
        for i in range(min_length):
            current_char = strs[0][i]
            if(all(s[i]==current_char for s in strs)):
                ans+=current_char
            else:
                break
        return ans