class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s=Counter(s)
        t=Counter(t)
        '''
        if s==t:
            return True
        return False

        for key,value in s.items():
            if(key not in t):
                return False
            elif(t[key]!=value):
                return False
        return True
        '''
        if len(s) != len(t): return False

        sCount = collections.Counter(s)
        tCount = collections.Counter(t)

        for c in sCount:
            if c not in tCount:
                return False
            if tCount[c] != sCount[c]:
                return False

        return True 