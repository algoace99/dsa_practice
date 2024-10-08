class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        for n in nums:
            i = abs(n) - 1
            if i < len(nums) and nums[i] > 0:
                nums[i] = nums[i]*-1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().firstMissingPositive(nums),file=f)
exit(0)