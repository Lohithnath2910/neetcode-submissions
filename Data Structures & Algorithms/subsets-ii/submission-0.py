class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = []
        p = []
        nums.sort()
        def b(i):
            r.append(p[:])
            
            for k in range(i,len(nums)):
                if k > i and nums[k] == nums[k-1]:
                    continue
                p.append(nums[k])
                b(k+1)
                p.pop()
        
        b(0)

        return r