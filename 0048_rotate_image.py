class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
#         Transpose Logic
        for i in range(n):
            for j in range(n):
                if i < j:
                    print(i, j)
                    print(matrix[i][j], "swapped with", matrix[j][i])
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for l in matrix:
            l.reverse()
