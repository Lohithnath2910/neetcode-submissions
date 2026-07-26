class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        p = []

        def bt():
            if len(p) == len(nums):
                r.append(p[:])
                return
            
            for k in range(len(nums)):
                if nums[k] not in p:
                    p.append(nums[k])
                    bt()
                    p.pop()


        bt()
        return r