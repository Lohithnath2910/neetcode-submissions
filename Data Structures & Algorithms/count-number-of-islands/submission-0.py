class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        co = 0
        def df(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return False
            
            grid[r][c] = "0"
                
            df(r+1,c)
            df(r-1,c)
            df(r,c+1)
            df(r,c-1)
    
            return True 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if df(i,j):
                    co += 1
        return co
        
        
        