class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        k = 0
        j = len(nums) - 1

        while(k <= j):
            if(nums[k] == 0):
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp
                k += 1
                i += 1
            
            elif(nums[k] == 2):
                temp = nums[k]
                nums[k] = nums[j]
                nums[j] = temp
                j -= 1
            
            else:
                k += 1
        return nums
            
