# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertAtBeginning(self,head,node):
        node.next = head
        head = node
        return head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        while curr.next:
            next_node = curr.next
            curr.next = next_node.next
            head = self.insertAtBeginning(head, next_node)
        
        return head