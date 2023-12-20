class Solution:
    def countWays(self, n, k):
        if n == 0:
            return 0

        same_color, diff_color = 0, k

        for i in range(2, n + 1):
            same_color, diff_color = diff_color, (same_color + diff_color) * (k - 1) % (10**9 + 7)

        return (same_color + diff_color) % (10**9 + 7)