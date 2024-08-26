class Solution:
    def reverseVowels(self, s: str) -> str:
        li=list(s)
        v=set(['a','e','i','o','u','A','E','I','O','U'])
        l=0
        r=len(li)-1
        while l<r:
            if li[l] not in v:
                l+=1
                continue
            if li[r] not in v:
                r-=1
                continue
            if li[l] in v and li[r] in v:
                li[l],li[r]=li[r],li[l]
                l+=1
                r-=1
        return "".join(li)
            
