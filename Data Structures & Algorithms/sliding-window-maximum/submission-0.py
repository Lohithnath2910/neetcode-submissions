class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        i = 0
        j = i + k - 1

        while(j < len(nums)):
            c = max(nums[i:j+1])
            ans.append(c)
            i += 1
            j += 1
        return ans

        
        