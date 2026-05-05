# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases
        if not head or not head.next or k == 0:
            return head
        
        # Find length and tail
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        # Reduce k
        k = k % length
        
        # No rotation needed
        if k == 0:
            return head
        
        # Make circular linked list
        tail.next = head
        
        # Find new tail
        steps = length - k - 1
        newTail = head
        
        for _ in range(steps):
            newTail = newTail.next
        
        # New head
        newHead = newTail.next
        
        # Break the circle
        newTail.next = None
        return newHead
        newTail.next = None
        
        return newHead
