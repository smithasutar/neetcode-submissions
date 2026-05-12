# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        num1 = []
        num2 = []

        while curr1:
            num1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            num2.append(curr2.val)
            curr2 = curr2.next

        num1.reverse()
        num2.reverse()

        number1 = 0
        number2 = 0

        for n in num1:
            number1 = number1*10+n
        for n in num2:
            number2 = number2*10+n

        number3 = number1+number2

        num3 = list(map(int, str(number3)))
        num3.reverse()
        new_head = ListNode(0)
        new_curr = new_head

        for n in num3:
            new_curr.next = ListNode(n)
            new_curr = new_curr.next
        
        return new_head.next







