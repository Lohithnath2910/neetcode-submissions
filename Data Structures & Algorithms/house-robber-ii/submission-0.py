class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nn1 = [0]*n
        nn2 = [0]*n
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[1], nums[0])

        nn1[0] = nums[0]
        nn1[1] = max(nums[0],nums[1])
        for i in range(2,n-1):
            nn1[i] = max(nn1[i-2] + nums[i], nn1[i-1])  
        
        nn2[1] = nums[1]
        nn2[2] = max(nums[1],nums[2])
        for i in range(3,n):
            nn2[i] = max(nn2[i-2] + nums[i], nn2[i-1])  
        
        return max(nn1[n-2], nn2[n-1])