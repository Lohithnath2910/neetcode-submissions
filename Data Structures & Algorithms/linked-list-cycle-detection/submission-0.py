# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        o = head
        t = head

        while(o != None and o.next != None and t != None and t.next != None):
            o = o.next
            t = (t.next).next
            if(o == t):
                return True
        
        return False
        