class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def df(i,j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] != "O":
                return
            
            board[i][j] = "T"
            df(i+1,j)
            df(i,j+1)
            df(i-1,j)
            df(i,j-1)
        
        
        for i in range(len(board)):
            if board[i][0] == "O":
                df(i,0)
            if board[i][len(board[0])-1] == "O":
                df(i,len(board[0])-1)

        for i in range(len(board[0])):
            if board[0][i] == "O":
                df(0,i)
            if board[len(board)-1][i] == "O":
                df(len(board)-1,i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"