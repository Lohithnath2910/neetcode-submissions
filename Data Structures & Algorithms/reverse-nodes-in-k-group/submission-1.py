# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        d = ListNode()
        d.next = head
        gp = d

        while True:
            kt = self.gk(gp,k)

            if not kt:
                break

            gn = kt.next

            prev = gn
            curr = gp.next

            while(curr != gn):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = gp.next
            gp.next = kt
            gp = temp
        return d.next


    def gk(self,h,k):
        while(k > 0 and h != None):
            h = h.next
            k-=1
        return h