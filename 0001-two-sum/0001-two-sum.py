class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        # works only for sorted array
        # Space = O(1)
        # Time = O(n)
        start=0
        end=len(nums)-1
        while(start<end):
            if(nums[start]+nums[end]==target):
                return [start,end]
            elif(nums[start]+nums[end]<target):
                start+=1
            else:
                end-=1
        '''
        '''
        # Time = O(n*n)
        # Space = O(1)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        '''
        # Space = O(n)
        # Time = O(n)
        h = {}
        for i in nums:
            h[i] = i
        for i in range(len(nums)):
            req = target - nums[i]
            if req in h:
                if req != nums[i]:
                    return [i, nums.index(req)]
                elif nums.count(nums[i])>1:
                    return [n for n in range(len(nums)) if nums[n]==req][:3]
