class Solution:
    def romanToInt(self, s: str) -> int:
        #if the next num is greater then substract i from i+1
        #if the number contains even numbers then add the last digit in the ending
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=0
        i=0
        while(i<len(s)-1):
            if(d[s[i]]<d[s[i+1]]):
                ans+=(d[s[i+1]]-d[s[i]])
                i+=2
            else:
                ans+=d[s[i]]
                i+=1
        if i == len(s) - 1:
            ans += d[s[i]]
        return ans

