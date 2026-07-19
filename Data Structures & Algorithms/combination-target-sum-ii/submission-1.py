class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def b(i,s,n):
            if n==target:
                res.append(s[:])
                return
            if n > target or i == len(candidates):
                return
            
            s.append(candidates[i])
            b(i+1,s,n+candidates[i])
            s.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            b(i+1,s,n)
        b(0,[],0)
        return res