class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return True if len(nums)!=len(list(set(nums))) else False
        if(len(set(nums))!=len(nums)):
            return True
        else:
            return False
        '''
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
        '''