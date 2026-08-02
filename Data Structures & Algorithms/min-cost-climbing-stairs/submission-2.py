class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = [0]*len(cost)
        n[0] = cost[0]
        n[1] = cost[1]
        
        for i in range(2,len(cost)):
            n[i] = min(n[i-1],n[i-2]) + cost[i]
        return min(n[len(cost)-1],n[len(cost)-2])

        
