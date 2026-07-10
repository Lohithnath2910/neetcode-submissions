# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = None
        ans = None
        while(list1 != None and list2 != None):
            if(list1.val < list2.val):
                if(l == None):
                    l = list1
                    ans = l
                    list1 = list1.next
                else:
                    t = list1
                    l.next = t
                    l = l.next
                    list1 = list1.next

            else:
                if(l == None):
                    l = list2
                    ans = l
                    list2 = list2.next
                else:
                    t = list2
                    l.next = t
                    l = l.next
                    list2 = list2.next
            
        while(list1 != None):
            if(l == None):
                l = list1
                ans = l
                list1 = list1.next
            else:     
                t = list1
                l.next = t
                l = l.next
                list1 = list1.next

        while(list2 != None): 
            if(l == None):
                l = list2
                ans = l
                list2 = list2.next
            else:     
                t = list2
                l.next = t
                l = l.next
                list2 = list2.next
    
        return ans        


                

        