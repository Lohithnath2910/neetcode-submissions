class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ro = [set() for x in range(9)]
        co = [set() for x in range(9)]
        boxes = [set() for x in range(9)]
         
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if(val == "."):
                    continue
                box = (r // 3)*3 + (c // 3)
                if(val in ro[r]):
                    return False
                elif(val in co[c]):
                    return False
                elif(val in boxes[box]):
                    return False
                ro[r].add(val)
                co[c].add(val)
                boxes[box].add(val)
        return True
        