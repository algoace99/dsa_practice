def sum1(a,b):
    return a+b
def sum2(a,b):
    return a+b
def sum3(a,b):
    return a+b
def sum4(a,b):
    return a+b
def sum5(a,b):
    return a+b
def sum6(a,b):
    return a+b

class Solution:
    def countElements(self, nums: List[int]) -> int:
        res = len(nums) - nums.count(min(nums)) - nums.count(max(nums))
        if res <= 0 :
            return 0
        return res