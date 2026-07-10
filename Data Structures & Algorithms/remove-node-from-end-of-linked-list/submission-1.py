# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0,head)
        temp1 = d
        temp2 = d
        while(temp1 != None):
            if(n != -1):
                temp1 = temp1.next
                n -= 1
            else:
                temp1 = temp1.next
                temp2 = temp2.next
                
        temp2.next = temp2.next.next
        
        return d.next