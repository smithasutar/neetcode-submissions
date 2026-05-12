# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        rev_head = prev

        i = 1
        dummy = ListNode(0, rev_head)
        prev1 = dummy
        cur1 = rev_head

        while cur1:
            if i == n:
                if prev1:
                    prev1.next = cur1.next
                    break
            prev1 = cur1
            cur1 = cur1.next
            i+=1

        cur = dummy.next
        prev = None

        while cur:
            temp1 = cur.next
            cur.next = prev
            prev = cur
            cur = temp1

        return prev