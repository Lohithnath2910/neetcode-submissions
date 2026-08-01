class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
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
        ans= []
        while(q):
            no = q.popleft()
            ans.append(no)
            for i in range(n):
                if mat[no][i]:
                    ind[i] -= 1
                    if ind[i] == 0 and not vis[i]:
                        vis[i] = 1
                        q.append(i)
        return ans if len(ans) == n else []