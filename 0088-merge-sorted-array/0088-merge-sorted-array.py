class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        elif n == 0:
            pass
        else:
            p1 = m - 1 
            p2 = n - 1 
            p = m + n - 1

            for i in range(m + n - 1, -1, -1):
                if p2 < 0:
                    break
                elif p1 >= 0 and nums1[p1] > nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[i] = nums2[p2]
                    p2 -= 1