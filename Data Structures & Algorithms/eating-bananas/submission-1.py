class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = sum(piles)
        i = 1
        j = max(piles)
        res = j
        while(i <= j):
            m = (i + j) // 2

            t = 0
            for p in piles:
                t += math.ceil(float(p)/m)
            if(t <= h):
                res = m
                j = m -1

            else:
                i = m + 1
        return res

        