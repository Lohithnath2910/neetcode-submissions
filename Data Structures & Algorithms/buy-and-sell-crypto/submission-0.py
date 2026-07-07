class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        m = prices[0]

        for i in prices:
            if(m > i):
                m = i
            pro = i - m
            if(pro > p):
                p = pro
        return p

        