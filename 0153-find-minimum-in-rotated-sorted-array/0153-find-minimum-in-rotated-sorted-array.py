class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return nums[i]
        return nums[0]
        '''
        #return min(nums)

        if len(nums)==1: return nums[0]
        if len(nums)==2: return min(nums)
        start=1
        end=len(nums)-1
        while(start<=end):
            m=start+(end-start)//2
            if nums[m]<nums[m-1]:
                return nums[m]
            elif nums[m]<nums[-1]:
                end=m-1
            else:
                start=m+1
        return nums[0]