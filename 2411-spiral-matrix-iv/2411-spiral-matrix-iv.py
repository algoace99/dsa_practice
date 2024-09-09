# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        a = [[0]*n for _ in range(m)]

        left = 0
        right = n-1
        top = 0
        bottom = m-1

        while left <= right and top <= bottom:
            #left to right
            for i in range(left, right+1):
                if head:
                    a[top][i] = head.val
                    head = head.next
                else:
                    a[top][i] = -1
            top+=1

            #top to bottom right side
            for i in range(top, bottom+1): # 1 to 3 -> 1,2
                if head:
                    a[i][right] = head.val
                    head = head.next
                else:
                    a[i][right] = -1
            right -=1

            if top <= bottom:
                #rght to left, bottom
                for i in range(right,left-1,-1):
                    if head:
                        a[bottom][i] = head.val
                        head = head.next
                    else:
                        a[bottom][i] = -1
                bottom-=1

            if left <= right:
                #bottom to top left side
                for i in range(bottom,top-1,-1):
                    if head:
                        a[i][left] = head.val
                        head = head.next
                    else:
                        a[i][left] = -1
                left+=1
        return a