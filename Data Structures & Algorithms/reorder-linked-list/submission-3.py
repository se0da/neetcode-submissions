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
        
        sec_head = slow.next
        slow.next = None
    
        prev, curr = None, sec_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        sec_head = prev

        dummy = ListNode()

        while sec_head and head:
            dummy.next = head
            head = head.next
            dummy = dummy.next

            dummy.next = sec_head
            sec_head = sec_head.next
            dummy = dummy.next
        
        dummy.next = head if head else sec_head
        
