# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            me = []
            for i in range(0,len(lists),2):
                t1 = lists[i]
                t2 = lists[i+1] if i + 1 < len(lists) else None
                me.append(self.m(t1,t2))
            lists = me
        
        return lists[0]


    def m(self,h,t):
        dum = ListNode()
        x = dum
        temp1 = h
        temp2 = t
        while(temp1 != None and temp2 != None):
            if(temp1.val < temp2.val):
                x.next = temp1
                temp1 = temp1.next
            else:
                x.next = temp2
                temp2 = temp2.next
            x = x.next
        
        x.next = temp1 or temp2

        return dum.next


    