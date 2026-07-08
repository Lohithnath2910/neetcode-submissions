class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0 , len(nums) - 1

        while(i <= j):
            m = (i+j) // 2
            if (target == nums[m]):
                return m

            if(nums[i] <= nums[m]):
                if(nums[i] > target or target > nums[m]):
                    i = m + 1
                else:
                    j = m - 1
            else:
                if(nums[m] > target or target > nums[j]):
                    j = m - 1
                else:
                    i = m + 1
        return -1
        