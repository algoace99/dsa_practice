class Solution:
    def countElements(self, nums: List[int]) -> int:
        res = len(nums) - nums.count(min(nums)) - nums.count(max(nums))
        if res <= 0 :
            return 0
        return res