class Solution:
    def maxGold(self, n, m, M):
        dp = [[0] * m for _ in range(n)]

        for col in range(m - 1, -1, -1):
            for row in range(n):
                current_gold = M[row][col]
                right = dp[row][col + 1] if col + 1 < m else 0
                up_right = dp[row - 1][col + 1] if row - 1 >= 0 and col + 1 < m else 0
                down_right = dp[row + 1][col + 1] if row + 1 < n and col + 1 < m else 0
                dp[row][col] = current_gold + max(right, up_right, down_right)

        max_gold = 0
        for row in range(n):
            max_gold = max(max_gold, dp[row][0])

        return max_gold

# https://www.geeksforgeeks.org/problems/gold-mine-problem2608/1