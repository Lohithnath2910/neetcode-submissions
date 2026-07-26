class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        p = []
        def bt(i):
            r.append(p[:])

            for i in range(i,len(nums)):
                p.append(nums[i])
                bt(i+1)
                p.pop()


        bt(0)
        return r
