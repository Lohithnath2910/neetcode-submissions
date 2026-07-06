class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        j = 0
        c = len(nums)
        while(j <= i):
            if(nums[j] == val):
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i -= 1
                c -= 1
            else:
                j += 1
        return c