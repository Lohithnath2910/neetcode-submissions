class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ns = nums[0]
        m1 = 1
        m2 = 1

        for i in nums:
            t = m1*i
            m1 = max(i*m1,i*m2,i)
            m2 = min(t,i*m2,i)
            ns = max(ns,m1)
        return ns