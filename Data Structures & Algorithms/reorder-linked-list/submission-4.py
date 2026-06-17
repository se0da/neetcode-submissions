# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        new_head = slow.next
        slow.next = None

        prev, cur = None, new_head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        new_head = prev
        res = dummy = ListNode()
        while head and new_head:
            dummy.next = head
            dummy = dummy.next
            head = head.next
            dummy.next = new_head
            dummy = dummy.next
            new_head = new_head.next

        dummy.next = head if head else new_head

