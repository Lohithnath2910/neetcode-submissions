class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        mat = [[0]*n for _ in range(n)]
        for a, b in p:
            mat[b][a] = 1

        ind = [0]*n
        vis = [0]*n

        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    ind[j] += 1
        
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                vis[i] = 1
                q.append(i)
        cnt = 0
        while(q):
            no = q.popleft()
            cnt += 1
            for i in range(n):
                if mat[no][i]:
                    ind[i] -= 1
                    if ind[i] == 0 and not vis[i]:
                        vis[i] = 1
                        q.append(i)
        return cnt == n
        


