import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        m = []
        for i in range(len(stones)):
            m.append(-stones[i])
        heapq.heapify(m)
        print(m)
        print(stones)
        while len(m) > 1:
            a = -(heapq.heappop(m))
            b = -(heapq.heappop(m))

            if a == b:
                continue
            
            elif a > b:
                f = a-b
                heapq.heappush(m,-f)
            
            else:
                f = b - a
                heapq.heappush(m,-f)
        return -(m[0]) if m else 0