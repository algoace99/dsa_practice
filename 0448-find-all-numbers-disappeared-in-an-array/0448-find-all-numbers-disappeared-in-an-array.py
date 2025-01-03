class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        s = set(nums)
        ans = []
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans
        '''
        for i in range(len(nums)):
            index = abs(nums[i]) - 1  #1-based to 0-based
            if nums[index] > 0:
                nums[index] = -nums[index]
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        
        return ans