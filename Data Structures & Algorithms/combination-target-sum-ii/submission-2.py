class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        p = []
        nums.sort()
        def bt(i):
            if sum(p) == target:
                r.append(p[:])
                return
            if sum(p) > target:
                return

            for k in range(i,len(nums)):
                if k > i and nums[k] == nums[k-1]:
                    continue
                p.append(nums[k])
                bt(k+1)
                p.pop()

        bt(0)
        return r