class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Time = O(n^2)
        # Space = O(n)
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    ans.append(words[i])
        return list(set(ans))