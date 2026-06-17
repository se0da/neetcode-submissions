# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of the list, disconnect it from the original list then reverse the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        new_head = slow.next
        slow.next = None
    
        prev, curr = None, new_head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head2 = prev

        res = dummy = ListNode()

        while head and head2:
            dummy.next = head
            head = head.next
            dummy = dummy.next

            dummy.next = head2
            head2 = head2.next
            dummy = dummy.next
        
        dummy.next = head if head else head2



        

