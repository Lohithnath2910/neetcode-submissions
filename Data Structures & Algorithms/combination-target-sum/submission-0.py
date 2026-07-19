class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(i,s,n):
            if n > target or i == len(nums):
                return
            if n == target:
                res.append(s[:])
                return
            s.append(nums[i])
            bt(i,s,n+nums[i])
            s.pop()
            bt(i+1,s,n)
        bt(0,[],0)
        return res