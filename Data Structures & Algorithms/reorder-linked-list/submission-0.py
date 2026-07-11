# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp1 = head
        temp2 = head
        while(temp2 != None and temp2.next != None):
            temp1 = temp1.next
            temp2 = temp2.next.next
        
        temp2 = temp1.next
        temp1.next = None
        
        x = self.r(temp2)

        f = head
       
        while(x != None):
            t1 = f.next
            t2 = x.next

            f.next = x
            x.next = t1

            f = t1
            x = t2 

    
    def r(self,h):
        curr = h
        prev = None
        nex = None

        while(curr != None):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

        
        