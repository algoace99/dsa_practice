class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k]==0):
                        a=[nums[i],nums[j],nums[k]]
                        a.sort()
                        if(a not in ans):
                            ans.append(a)
        return ans
        '''
        nums.sort()
        triplets = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate elements
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # skip duplicate elements
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # skip duplicate elements
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triplets