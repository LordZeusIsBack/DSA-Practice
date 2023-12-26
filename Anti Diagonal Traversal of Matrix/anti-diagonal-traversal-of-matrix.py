class Solution:
    def antiDiagonalPattern(self, matrix):
        result = []
        N = len(matrix)
        for d in range(N + N - 1):
            if d < N:
                i, j = 0, d
            else:
                i, j = d - N + 1, N - 1
            while i < N and j >= 0:
                result.append(matrix[i][j])
                i += 1
                j -= 1

        return result