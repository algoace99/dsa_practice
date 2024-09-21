class Solution:
    def convertToBase7(self, num: int) -> str:
        ans=""
        temp=num
        num = abs(num)
        while(num>0):
            ans+=str(num%7)
            num//=7
        neg_case="-"+ans[::-1]
        return ans[::-1] if temp>0 else "0" if temp==0 else neg_case