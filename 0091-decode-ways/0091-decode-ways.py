class Solution:
    def __init__(self):
        self.memo = []

    def backtrack(self, s, start):
        if start == len(s):
            return 1
        elif self.memo[start] != -1:
            return self.memo[start]
        else:
            ret = 0
            if s[start] != '0':
                ret += self.backtrack(s, start + 1)

                if start + 1 < len(s) and (s[start] == '1' or (s[start] == '2' and s[start + 1] <= '6')):
                    ret += self.backtrack(s, start + 2)

            self.memo[start] = ret
            return ret

    def numDecodings(self, s: str) -> int:
        self.memo = [-1] * len(s)
        return self.backtrack(s, 0)
