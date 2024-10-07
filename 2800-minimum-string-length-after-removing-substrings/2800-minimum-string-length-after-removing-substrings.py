class Solution:
    def minLength(self, s: str) -> int:
        if len(s)==1:
            return 1
        sta = []
        for i in s:
            print(sta)
            if len(sta) == 0:
                sta.append(i)
                continue
            if i=="B" and sta[-1]=="A":
                sta.pop()
            elif i=="D" and sta[-1]=="C":
                sta.pop()
            else:
                sta.append(i)
        return len(sta)