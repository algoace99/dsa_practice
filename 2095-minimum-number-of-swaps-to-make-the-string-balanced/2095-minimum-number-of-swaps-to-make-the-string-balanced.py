class Solution:
    def minSwaps(self, s: str) -> int:
        arr = []
        unbalanced = 0
        for i in s:
            if i=="[":
                arr.append(i)
            elif len(arr)!=0:
                arr.pop()
            else:
                unbalanced+=1
        return (unbalanced+1)//2