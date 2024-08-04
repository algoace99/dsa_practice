class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            d=list(i)
            d.sort()
            d="".join(d)
            if d in ans:
                ans[d].append(i)
            else:
                ans[d]=[i]
        return list(ans.values())
        '''
        ans=[]
        ans.append([strs[0]])
        for i in range(1,len(strs)):
            indi=0
            for j in range(len(ans)):
                a=list(ans[j][0])
                b=list(strs[i])
                if Counter(a)==Counter(b) and len(a)==len(b):
                    ans[j].append(strs[i])
                    indi=1
                    break
            if indi==0:
                ans.append([strs[i]])
        return ans
        '''