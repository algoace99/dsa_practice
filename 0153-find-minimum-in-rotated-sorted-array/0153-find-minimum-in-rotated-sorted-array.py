class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return nums[i]
        return nums[0]
        '''
        #return min(nums)

        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]