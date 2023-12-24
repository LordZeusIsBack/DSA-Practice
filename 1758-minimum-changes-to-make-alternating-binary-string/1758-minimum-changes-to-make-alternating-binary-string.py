class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            if s[i] != str(i % 2):
                res += 1
        return min(res, n - res)
