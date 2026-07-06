class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, j in enumerate(nums):
            compliment = target - j

            if compliment in d:
                return [d[compliment],i]
            
            d[j] = i
