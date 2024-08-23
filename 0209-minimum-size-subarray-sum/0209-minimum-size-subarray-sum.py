class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum_ele = 0
        min_len = float('inf')

        for r in range(len(nums)):
            sum_ele += nums[r]
            while sum_ele >= target:
                min_len = min(min_len,r-l+1)
                sum_ele -= nums[l]
                l+=1
        return min_len if min_len != float('inf') else 0