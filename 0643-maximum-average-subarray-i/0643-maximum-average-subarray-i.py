class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k
        s=sum(nums[l:r])
        av=s/k
        while(r<=len(nums)-1):
            s-=nums[l]
            s+=nums[r]
            internal_av=s/k
            av=max(av,internal_av)
            l+=1
            r+=1
        return av