class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i,j,0])
        
        while q:
            n = q.popleft()
            i = n[0]
            j = n[1]
            t = n[2]

            if i + 1 < len(grid) and grid[i+1][j] == 2147483647:
                grid[i+1][j] = min(t+1,grid[i+1][j])
                q.append([i+1,j,t+1])

            if j + 1 < len(grid[0]) and grid[i][j+1] == 2147483647:
                grid[i][j+1] = min(t+1,grid[i][j+1])
                q.append([i,j+1,t+1])

            if i - 1 >= 0 and grid[i-1][j] == 2147483647:
                grid[i-1][j] = min(t+1,grid[i-1][j])
                q.append([i-1,j,t+1])

            if j - 1 >= 0 and grid[i][j-1] == 2147483647:
                grid[i][j-1] = min(t+1,grid[i][j-1])
                q.append([i,j-1,t+1])