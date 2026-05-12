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

        new_head = Node(0)
        new_curr = new_head

        curr = head
        legend = {None:None}

        while curr:
            new_curr.next = Node(curr.val)
            new_curr = new_curr.next
            legend[curr] = new_curr
            curr = curr.next

        curr = head
        new_curr = new_head.next

        while curr:
            new_curr.random = legend[curr.random]
            new_curr = new_curr.next
            curr = curr.next

        return new_head.next





        