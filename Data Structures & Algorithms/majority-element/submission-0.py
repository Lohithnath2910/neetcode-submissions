class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        k = nums[0]
        for i in range(1,len(nums)):
            if (k != nums[i] and c == 0):
                k = nums[i]
                c = 1
            elif (k == nums[i]):
                c += 1
            else:
                c -= 1
        
        c2 = 0
        for i in nums:
            if(i == k):
                c2 += 1
        
        if(c2 > len(nums)/2):
            return k
        return -1

        