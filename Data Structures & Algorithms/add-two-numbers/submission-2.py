# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = l1
        a2 = l2

        n1 = self.c(a1)
        n2 = self.c(a2)

        n = n1 + n2
        temp = ListNode()
        d = temp
        if(n == 0):
            return d

        while(n != 0):
            aa = n%10
            n //= 10

            z = ListNode(aa)
            temp.next = z
            temp = temp.next
        return d.next


    def c(self,k):
        s = 0
        f = 1
        while(k != None):
            s += f*(k.val)
            f *= 10
            k = k.next
        return s
