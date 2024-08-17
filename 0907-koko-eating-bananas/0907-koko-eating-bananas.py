class Solution:
    def is_valid(self, num,piles):
        ans=0
        for i in piles:
            ans+=math.ceil(i/num)
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)
        while(start<end):
            mid=start+(end-start)//2
            ans=self.is_valid(mid,piles)
            if ans<=h:
                end=mid
            else:
                start=mid+1
        return end