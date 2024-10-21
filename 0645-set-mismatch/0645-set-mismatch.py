class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = 0
        for i in range(n):
            val = abs(nums[i])
            j = val - 1
            if nums[j] < 0:
                dup = val
            total += val
            nums[j] = -nums[j]

        diff = total - (1 + n) * n // 2
        miss = dup - diff

        return [dup, miss]