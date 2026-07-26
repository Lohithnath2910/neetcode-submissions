class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        s = set()

        def b(i,r,c):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False 
            if board[r][c] != word[i]:
                return False
            
            if (r,c) in s:
                return False 
            s.add((r, c))
            found = (b(i+1, r+1, c) or      
                     b(i+1, r-1, c) or
                     b(i+1, r, c+1) or      
                     b(i+1, r, c-1))  

            s.remove((r, c))
            return found
            
        for r in range(rows):       
            for c in range(cols):
                if b(0, r, c):
                    return True
        return False