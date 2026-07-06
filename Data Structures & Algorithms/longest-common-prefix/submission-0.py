class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        while a:
            ok = True

            for i in strs:
                if not i.startswith(a):
                    ok = False
                    break

            if ok:
                return a
            
            a = a[:-1]

        return ""
        