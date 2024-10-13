import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        best_range = [-float('inf'), float('inf')]
        
        while min_heap:
            current_min, list_idx, element_idx = heapq.heappop(min_heap)

            if current_max - current_min < best_range[1] - best_range[0]:
                best_range = [current_min, current_max]
            
            if element_idx + 1 < len(nums[list_idx]):
                next_element = nums[list_idx][element_idx + 1]
                heapq.heappush(min_heap, (next_element, list_idx, element_idx + 1))
                current_max = max(current_max, next_element)
            else:
                break
        
        return best_range