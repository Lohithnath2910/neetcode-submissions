# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = None
        nex = head
        while nex != None:
            curr = nex
            nex = nex.next
            curr.next = prev
            prev = curr
        return curr
        