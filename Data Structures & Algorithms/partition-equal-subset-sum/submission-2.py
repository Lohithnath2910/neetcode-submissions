class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k = sum(nums)
        n = len(nums)
        h = k // 2

        if k % 2 != 0:
            return False

        dp = [False]*(h+1)

        dp[0] = True

        for i in nums:
            for j in range(h-i,-1,-1):
                if dp[j]:
                    dp[j+i] = True

        return dp[h]