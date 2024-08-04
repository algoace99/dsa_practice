class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        count=0
        k=0
        for key,value in d.items():
            if(count<value):
                count=value
                k=key
        return k
