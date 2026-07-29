class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows,cols = len(heights), len(heights[0])
        k1 = set()
        k2 = set()

        def df(r,c,v,p):
            if ((r,c) in v or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < p):
                return
            
            v.add((r,c))

            df(r+1,c,v,heights[r][c])
            df(r,c+1,v,heights[r][c])
            df(r-1,c,v,heights[r][c])
            df(r,c-1,v,heights[r][c])

        for c in range(cols):
            df(0,c,k1,heights[0][c])
            df(rows-1,c,k2,heights[rows-1][c])

        for r in range(rows):
            df(r,0,k1,heights[r][0])
            df(r,cols-1,k2,heights[r][cols-1])

        for r in range(rows):
            for c in range(cols):
                if((r,c) in k1 and (r,c) in k2):
                    res.append([r,c])

        return res