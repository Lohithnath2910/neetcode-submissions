class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for i,j in enumerate(points):
            m = math.sqrt((j[0])**2 + (j[1])**2)
            f = (m,i)
            ans.append(f)
        heapq.heapify(ans)
        l = []
        for i in range(k):
            te = heapq.heappop(ans)
            l.append([points[te[1]][0],points[te[1]][1]])
        return l

        