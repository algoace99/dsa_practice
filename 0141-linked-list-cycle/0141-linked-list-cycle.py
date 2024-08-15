# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None or head.next.next==None:
            return False

        slow=head
        fast=head.next.next
        while head:
            if slow==fast:
                return True
            elif fast.next==None or fast.next.next==None:
                return False
            else:
                fast=fast.next.next
                slow=slow.next
        return False