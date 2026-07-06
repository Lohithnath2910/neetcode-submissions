class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        f = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        for i in t:
            f[i] = f.get(i,0) + 1

        return d == f