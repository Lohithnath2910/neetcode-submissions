class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        p = []

        def bt(i):
            if sum(p) == target:
                r.append(p[:])
                return 
            
            if sum(p) > target:
                return
            
            for k in range(i,len(nums)):
                p.append(nums[k])
                bt(k)
                p.pop()
        bt(0)
        return r