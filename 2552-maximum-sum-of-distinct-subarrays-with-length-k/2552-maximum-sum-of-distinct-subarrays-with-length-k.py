class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = Counter(nums[:k])
        current_sum = sum(nums[:k])
        max_sum = 0
        if len(d) == k:
            max_sum = current_sum

        for i in range(k,len(nums)):
            current_sum = current_sum + nums[i] - nums[i-k]
            d[nums[i]] += 1
            if nums[i-k] in d:
                d[nums[i-k]] -= 1
                if d[nums[i-k]] <= 0:
                    del d[nums[i-k]]
            if len(d) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum