"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        my_map = {}
        if head is None:
            return None

        while temp:
            my_map[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            if temp.next:
                my_map[temp].next = my_map[temp.next]
            if temp.random:
                my_map[temp].random = my_map[temp.random]
            temp = temp.next
        
        return my_map[head]

