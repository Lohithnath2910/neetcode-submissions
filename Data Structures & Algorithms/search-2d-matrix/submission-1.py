class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0])*len(matrix) - 1
        while(i <= j):
            mid = (i + j) // 2
            mr = mid // len(matrix[0])
            mc = mid % len(matrix[0])
            if(matrix[mr][mc] == target):
                return True
            elif(matrix[mr][mc] > target):
                j -= 1
            else:
                i += 1
        return False
        