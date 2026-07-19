class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = []

        def b(s):
            if len(s) == len(nums):
                p.append(s[:])
                return

            for i in nums:
                if i in s:
                    continue
                
                s.append(i)
                b(s)
                s.pop()
        
        b([])
        return p