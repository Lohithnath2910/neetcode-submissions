class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        t1 = 1
        t2 = 2
        h = 0
        for i in range(2,n):
            t3 = t1 + t2
            t1,t2,t3 = t2,t3,t1 + t2
            h = t3
        return h