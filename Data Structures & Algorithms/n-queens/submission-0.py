class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        re = []
        p = []
        col = set()
        diag1 = set()
        diag2 = set()

        def b(r):
            if r == n:

                bo = []
                for c in p:
                    s = (".")*c+"Q"+(".")*(n-c-1)
                    bo.append(s)
                re.append(bo)
                return
            
            for c in range(n):
                if c in col or (r-c) in diag1 or (r+c) in diag2:
                    continue
                
                p.append(c)
                col.add(c)
                diag1.add(r-c)
                diag2.add(r+c)

                b(r+1)

                p.pop()
                col.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)

        b(0)
        return re