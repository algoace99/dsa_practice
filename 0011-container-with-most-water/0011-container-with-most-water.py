class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height)-1
        while start < end:
            h = min(height[start],height[end])
            area = h*(end-start)
            max_area = max(max_area,area)
            if height[start] < height[end]:
                start +=1
            else:
                end -= 1
        return max_area