class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split()) 
        s2 = Counter(s2.split())

        ans = []
        for i in s1.items():
            if i[0] not in s2 and i[1]==1:
                ans.append(i[0])
        for i in s2.items():
            if i[0] not in s1 and i[1]==1:
                ans.append(i[0])
        return ans