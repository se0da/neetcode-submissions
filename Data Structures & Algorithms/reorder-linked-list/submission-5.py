# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        sec_head = slow.next
        prev, cur = None, sec_head
        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        sec_head = prev

        res = dummy = ListNode()

        while head or sec_head:
            if head:
                dummy.next = head 
                dummy = dummy.next
                head = head.next
            if sec_head:
                dummy.next = sec_head
                dummy = dummy.next
                sec_head = sec_head.next

        