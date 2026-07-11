class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 0
        f = 0
        while((s == 0 and f == 0) or s != f):
            s = nums[s]
            f = nums[nums[f]]
        s = 0

        while(s != f):
            s = nums[s]
            f = nums[f]

        return s
        
        