class Solution:
    def partition(self, s: str) -> List[List[str]]:
        r = []
        p = []

        def isp(s1):
            return s1 == s1[::-1]

        def b(s11,i):
            if i == len(s):
                r.append(p[:])
                return
            
            
            for k in range(i,len(s)):
                s11 = s[i:k+1]
                if isp(s11):
                    p.append(s11)
                    b(s11,k+1)
                    p.pop()

        b("",0)

        return r