class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t1 = {}
        w = {}

        for c in t:
            t1[c] = t1.get(c, 0) + 1

        h = 0
        n = len(t1)

        i = 0

        res =[-1,-1]
        resl = float("inf")

        for j in range(len(s)):
            c = s[j]

            w[c] = w.get(c,0) + 1

            if c in t1 and w[c] == t1[c]:
                h += 1
            
            while h == n:
                if (j-i+1) < resl:
                    res = [i,j]
                    resl = j-i+1
                
                w[s[i]] -= 1
                
                if s[i] in t1 and w[s[i]] < t1[s[i]]:
                    h -= 1
                i += 1

        l,r = res
        

        return "" if resl == float("inf") else s[l:r+1]
        