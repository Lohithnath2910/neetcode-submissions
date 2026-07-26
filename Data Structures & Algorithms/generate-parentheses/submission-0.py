class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        re = []
        def b(i,l,r,p):
            if i == 2*n:
                re.append(p)
                return
            if l < n:
                p+="("
                b(i+1,l+1,r,p)
                p = p[:-1]
            if r < l:
                p+=")"
                b(i+1,l,r+1,p)
                
        
        b(0,0,0,"")

        return re