class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix == None or len(matrix) == 0: return 0
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    if i != 0 and j != 0:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    res += matrix[i][j]
        
        return res