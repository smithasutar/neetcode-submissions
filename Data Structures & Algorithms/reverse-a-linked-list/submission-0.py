# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        prev = None
        while curNode:
            next_node = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = next_node
        return prev
        