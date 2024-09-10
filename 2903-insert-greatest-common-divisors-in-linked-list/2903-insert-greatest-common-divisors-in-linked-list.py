import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp_head = head
        while head.next:
            gcd = math.gcd(head.val, head.next.val)
            new_node = ListNode(gcd)
            temp = head.next
            head.next = new_node
            new_node.next = temp

            head = head.next.next
        return temp_head