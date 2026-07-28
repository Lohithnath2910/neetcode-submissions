class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ar = 0
        co = 0
        def df(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + df(r + 1, c) + df(r, c + 1) + df(r - 1, c) + df(r, c - 1)

        for i in range(len(grid)):
            co = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ar = max(df(i,j),ar)
                    
        return ar