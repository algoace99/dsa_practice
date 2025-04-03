class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        # l = 0
        # r = len(nums)-1
        # while l < r:
        #     if nums[l]+nums[r] == target:
        #         return [l, r]
        #     elif nums[l]+nums[r] < target:
        #         l += 1
        #     else:
        #         r -= 1
        