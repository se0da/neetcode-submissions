# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev, curr = None, second

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        second = prev

        dummy = node = ListNode()

        while head and second:
            node.next = head
            head = head.next
            node = node.next
            node.next = second 
            second = second.next
            node = node.next
        
        node.next = head or second
