class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        s.append(0)
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                idx = s.pop()
                ans[idx] = i - idx
            s.append(i) 
        return ans
                    
                    


        