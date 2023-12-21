class Solution:
    def nthPoint(self, n):
        a = b = 1

        mod = 10**9 + 7

        for i in range(1, n):
            c = (a + b) % mod
            a, b = b, c

        return b

# https://www.geeksforgeeks.org/problems/reach-the-nth-point5433/1