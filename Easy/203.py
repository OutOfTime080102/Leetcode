# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Check if the head is None
        while head and head.val == val:
            head = head.next
        
        current = head
        while current:
            # Check if the next node's value is equal to val
            while current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        
        return head
