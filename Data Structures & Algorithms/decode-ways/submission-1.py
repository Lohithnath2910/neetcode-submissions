class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def f(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0

            ans = f(i+1)

            if i < len(s) -1:
                if s[i] == "1" or (s[i] == "2" and s[i+1] < "7"):
                    ans += f(i+2) 
                    


            dp[i] = ans
            return ans

        return f(0)