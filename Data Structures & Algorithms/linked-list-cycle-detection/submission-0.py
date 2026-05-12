# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curNode = head
        hashmap = set()

        while curNode:
            if curNode not in hashmap:
                hashmap.add(curNode)
            else:
                return True
            
            curNode = curNode.next

        return False