from typing import List


class Solution:
    def sumZeroMatrix(self, a: List[List[int]]) -> List[List[int]]:
        n = len(a)
        m = len(a[0])

        rowPrefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                rowPrefix[i][j] += rowPrefix[i][j - 1] + a[i - 1][j - 1]

        best = 0
        sx, sy, ex, ey = 0, 0, 0, 0

        for i in range(1, m + 1):
            for j in range(i, m + 1):
                pre = {0: 0}
                csum = 0

                for k in range(1, n + 1):
                    csum += rowPrefix[k][j] - rowPrefix[k][i - 1]

                    if csum in pre:
                        area = (j - i + 1) * (k - pre[csum])

                        if area > best:
                            best = area
                            sx, sy, ex, ey = pre[csum] + 1, i, k, j
                    else:
                        pre[csum] = k

        if best == 0:
            return []

        ans = [a[i - 1][sy - 1:ey] for i in range(sx, ex + 1)]
        return ans