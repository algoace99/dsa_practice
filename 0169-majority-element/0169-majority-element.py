class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ans=0
        for i in nums:
            if count==0:
                ans=i
                count=1
            elif(ans==i):
                count+=1
            else:
                count-=1
        return ans
        '''
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
        '''