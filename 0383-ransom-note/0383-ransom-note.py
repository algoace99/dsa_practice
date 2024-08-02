class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m=Counter(magazine)
        r=Counter(ransomNote)
        for key,value in r.items():
            if(key not in m):
                return False
            elif(value>m[key]):
                return False
        return True