import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.m = nums
        heapq.heapify(self.m)
        
        while len(self.m) > self.k:
            heapq.heappop(self.m)


    def add(self, val: int) -> int:
        heapq.heappush(self.m,val)
        if len(self.m) > self.k:
            heapq.heappop(self.m)
        return self.m[0]
