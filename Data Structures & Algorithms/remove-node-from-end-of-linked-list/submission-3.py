# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        prev = res = ListNode()
        prev.next, curr = head, head
        while n:
            curr = curr.next
            n -= 1
        while curr is not None:
            prev = prev.next
            curr = curr.next
        prev.next = prev.next.next
        return res.next


            
