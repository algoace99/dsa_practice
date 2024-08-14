# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        # Determine the starting point of the merged list
        if list1.val < list2.val:
            current = list1
            dummy=current
            list1 = list1.next
        else:
            current = list2
            dummy=current
            list2 = list2.next


        # Merge by adjusting pointers
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy