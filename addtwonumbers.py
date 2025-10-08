# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a single node in the linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

class Solution:
    def addTwoNumbers(self, list1, list2):
        start = ListNode(0)
        current = start
        carry = 0

        while list1 or list2 or carry:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

           
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next

        return start.next
