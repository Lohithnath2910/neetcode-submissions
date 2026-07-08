class MinStack:

    def __init__(self):
        self.s = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        
    def pop(self) -> None:
        if(len(self.s) != 0):
            self.s.pop()
        
    def top(self) -> int:
        if(len(self.s) != 0):
            return self.s[-1]
        
    def getMin(self) -> int:
        if(len(self.s) != 0):
            return min(self.s)
        
