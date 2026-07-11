"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        l = {}
        temp = head

        while(temp != None):
            f = Node(temp.val)
            l[temp] = f
            temp = temp.next
        
        temp = head
        while(temp != None):
            l[temp].next = l[temp.next] if temp.next else None
            temp = temp.next
        
        temp = head
        while(temp != None):
            l[temp].random = l[temp.random] if temp.random else None
            temp = temp.next
        

        return l[head] if head else None

        