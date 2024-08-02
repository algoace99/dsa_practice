class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        s=set(jewels)
        for i in stones:
            if i in s:
                c+=1
        return c