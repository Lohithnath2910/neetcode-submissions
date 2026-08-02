class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nn = [0]*n
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[1], nums[0])

        nn[0] = nums[0]
        nn[1] = max(nums[0],nums[1])

        for i in range(2,n):
            nn[i] = max(nn[i-2] + nums[i], nn[i-1])  


        return max(nn[n-1], nn[n-2])