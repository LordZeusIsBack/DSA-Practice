class Solution:

    def determinantOfMatrix(self, matrix, n):
        if n == 1:
            return matrix[0][0]

        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0

        for i in range(n):
            cofactor = ((-1) ** i) * matrix[0][i] * self.determinantOfMatrix(self.getSubmatrix(matrix, n, i), n - 1)
            det += cofactor

        return det

    def getSubmatrix(self, matrix, n, col):
        submatrix = [[0] * (n - 1) for _ in range(n - 1)]
        for i in range(1, n):
            submatrix[i - 1] = matrix[i][:col] + matrix[i][col + 1:]
        return submatrix