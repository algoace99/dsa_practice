class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        # Step 1: Calculate the maximum possible bitwise OR of the entire array
        for num in nums:
            maxOr |= num
        
        # Step 2: Helper function with memoization
        def countSubsets(index, currentOr):
            # Base case: if all elements are processed
            if index == len(nums):
                return 1 if currentOr == maxOr else 0
            
            # Recursively explore both include and exclude options
            include = countSubsets(index + 1, currentOr | nums[index])
            exclude = countSubsets(index + 1, currentOr)
            
            return include + exclude

        # Step 3: Start from index 0 with OR value of 0
        return countSubsets(0, 0)