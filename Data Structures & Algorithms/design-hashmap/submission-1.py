class MyHashMap:

    def __init__(self):
        self.s = {}

    def put(self, key: int, value: int) -> None:
        self.s[key] = value

    def get(self, key: int) -> int:
        return self.s.get(key,-1)
        

    def remove(self, key: int) -> None:
        self.s.pop(key,None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)