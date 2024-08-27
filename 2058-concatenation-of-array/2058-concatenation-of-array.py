class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        ans = nums
        ans += nums
        return ans
        '''
        nums.extend(nums)
        return nums