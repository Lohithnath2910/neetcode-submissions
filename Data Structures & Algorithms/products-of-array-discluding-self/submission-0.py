class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lis1 = [1]*len(nums)
        lis1[0] = nums[0]
        for i in range(1,len(nums)):
            lis1[i] = lis1[i-1]*nums[i]
        lis2 = [1]*len(nums)
        lis2[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            lis2[i] = lis2[i+1]*nums[i]

        for i in range(len(nums)):
            if(i == 0):
                nums[i] = lis2[i+1]
            elif(i == len(nums)-1):
                nums[i] = lis1[i-1]
            else:
                nums[i] = lis1[i-1] * lis2[i+1]

        return nums