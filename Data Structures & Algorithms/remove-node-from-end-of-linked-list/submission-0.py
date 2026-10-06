# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        dummy = ListNode(0, head)
        prev = dummy
        current = head

        target = length - n

        for _ in range(target):
            prev = current
            current = current.next

        prev.next = current.next

        return dummy.next