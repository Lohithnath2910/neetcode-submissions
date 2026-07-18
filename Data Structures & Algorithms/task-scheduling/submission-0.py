class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        time = 0
        arr = {}

        for i in tasks:
            if i in arr:
                arr[i] += 1
            else:
                arr[i] = 1

        l = []
        for i in arr:
            l.append(arr[i])
        
        heapq.heapify_max(l)
        q = deque()

        while(q or l):
            time += 1
            
            if l:
                t = heapq.heappop_max(l) - 1
                if t > 0:
                    q.append([t,time+n])

            if q and q[0][1] == time:
                heapq.heappush_max(l,q.popleft()[0])
                

        return time
        