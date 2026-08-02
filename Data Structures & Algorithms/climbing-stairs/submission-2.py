class Solution:
    def climbStairs(self, n: int) -> int:
        ne = [0]*(n+1)
        ne[0] = 1
        ne[1] = 2

        for i in range(2,n):
            ne[i] = ne[i-1] + ne[i-2]
        return ne[n-1]