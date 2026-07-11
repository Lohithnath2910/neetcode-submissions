class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.h = Node(0,0)
        self.t = Node(0,0)
        
        self.h.next = self.t
        self.t.prev = self.h

    def rem(self,node):
        p = node.prev
        n = node.next

        p.next = n
        n.prev = p

    def ins(self,node):
        p = self.t.prev

        p.next = node
        node.prev = p

        node.next = self.t
        self.t.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.rem(node) 
        self.ins(node) 
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.rem(self.cache[key])
        
        node = Node(key,value)

        self.cache[key] = node
        self.ins(node)

        if len(self.cache) > self.capacity:
            lru = self.h.next
            self.rem(lru)
            del self.cache[lru.key]
        
