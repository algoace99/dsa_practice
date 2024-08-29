class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            c+=min(nums[i]%3, 3-(nums[i]%3))
        return c